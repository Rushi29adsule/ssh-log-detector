import re
import subprocess
from collections import Counter

print("\n===== SSH LOG DETECTOR v3.0 =====")

command = [
    "journalctl",
    "-u", "ssh",
    "--no-pager",
    "-o", "short-iso"
]

result = subprocess.run(
    command,
    capture_output=True,
    text=True
)

events = []
ip_counts = Counter()

for line in result.stdout.splitlines():

    if "Failed password" in line:

        match = re.search(
            r"Failed password for (?:invalid user )?(\S+) from (\d{1,3}(?:\.\d{1,3}){3})",
            line
        )

        if match:
            timestamp = line.split()[0]
            username = match.group(1)
            ip_address = match.group(2)

            events.append({
                "timestamp": timestamp,
                "username": username,
                "ip": ip_address
            })

            ip_counts[ip_address] += 1

print("\n===== SECURITY EVENT REPORT =====")

for event in events:

    ip = event["ip"]
    attempts = ip_counts[ip]

    if attempts >= 5:
        severity = "HIGH"
    elif attempts >= 3:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    print("\nTimestamp:", event["timestamp"])
    print("Username:", event["username"])
    print("Source IP:", ip)
    print("Total IP Attempts:", attempts)
    print("Severity:", severity)
    print("----------------------------")


import csv

with open("security_report.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["timestamp", "username", "ip"])
    writer.writeheader()
    writer.writerows(events)

print("\nCSV Security Report Generated Successfully!")
