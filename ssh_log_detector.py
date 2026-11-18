import re
import subprocess
from collections import Counter

THRESHOLD = 3

command = [
    "journalctl",
    "-u", "ssh",
    "--no-pager",
    "-o", "cat"
]

result = subprocess.run(
    command,
    capture_output=True,
    text=True,
    check=True
)

failed_ips = Counter()
failed_users = Counter()

for line in result.stdout.splitlines():

    match = re.search(
        r"Failed password for (?:invalid user )?(\S+) from (\d{1,3}(?:\.\d{1,3}){3})",
        line
    )

    if match:
        username = match.group(1)
        ip = match.group(2)

        failed_ips[ip] += 1
        failed_users[username] += 1

print("\n===== SSH LOG DETECTOR v2.0 =====")

if not failed_ips:
    print("No failed SSH login attempts found.")

for ip, count in failed_ips.most_common():

    print(f"\nSource IP: {ip}")
    print(f"Failed attempts: {count}")

    if ip == "192.168.59.129":
        print("Source: Ubuntu (local lab machine)")
    elif ip == "192.168.59.128":
        print("Source: Kali (lab machine)")
    else:
        print("Source: Unknown")

    if count >= THRESHOLD:
        print("ALERT: Threshold reached!")

print("\n===== USERNAME SUMMARY =====")

for username, count in failed_users.most_common():
    print(f"{username}: {count} attempts")
