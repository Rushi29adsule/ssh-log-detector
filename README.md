# SSH Log Detector – Python Cybersecurity Project

## Project Overview

The SSH Log Detector is a Python-based cybersecurity project developed in an Ubuntu and Kali Linux virtual machine lab.

It analyzes SSH authentication logs to identify failed login attempts, extract usernames and source IP addresses, count repeated attempts, and assign severity levels based on the number of attempts.

The project demonstrates basic security log analysis and suspicious login activity monitoring.

## Objectives

- Analyze SSH authentication logs.
- Detect failed SSH login attempts.
- Extract timestamps, usernames, and source IP addresses.
- Count failed attempts from each IP address.
- Assign severity levels to detected activity.
- Generate a CSV report for further analysis.

## Technologies Used

- Python 3
- Ubuntu Linux
- Kali Linux
- VMware Workstation
- Linux `journalctl`
- SSH authentication logs
- CSV

## Project Features

1. **SSH Log Analysis:** Reads SSH service logs using `journalctl`.
2. **Failed Login Detection:** Identifies failed password authentication events.
3. **IP Address Tracking:** Counts failed login attempts associated with each source IP.
4. **Severity Classification:**
   - HIGH: 5 or more failed attempts
   - MEDIUM: 3–4 failed attempts
   - LOW: Fewer than 3 failed attempts
5. **CSV Report Generation:** Exports timestamps, usernames, and IP addresses into a CSV file.

## How It Works

1. The script retrieves SSH service logs from the Linux system.
2. It searches for failed password authentication events.
3. It extracts the timestamp, username, and source IP address.
4. It counts the failed attempts associated with each IP.
5. It assigns a severity level based on the attempt count.
6. It generates a CSV report containing the detected events.

## Project Files

| File | Description |
|---|---|
| `ssh_log_detector.py` | Earlier version of the SSH log detector |
| `ssh_log_detector_v2.py` | Version 2 with IP and username counting |
| `ssh_log_detector.v3.py` | Version 3 with timestamps, severity classification, and CSV export |
| `security_report.csv` | CSV report of detected failed login events |
| `security_report.txt` | Text-based security event report |
| `ip_summary.txt` | Summary of failed attempts by IP address |
| `Screenshots/` | Project execution and output screenshots |

## Installation and Execution

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd ssh-log-detector
```

Replace `YOUR_REPOSITORY_URL` with your GitHub repository URL.

### 2. Check Python installation

```bash
python3 --version
```

### 3. Run the detector

```bash
sudo python3 ssh_log_detector.v3.py
```

The script reads SSH service logs using `journalctl`. Appropriate permissions and SSH service logs are required.

### 4. View the generated CSV report

```bash
cat security_report.csv
```

## Sample Results

The lab testing demonstrated that the detector could identify repeated failed SSH login attempts from different lab IP addresses.

The script classified activity using the configured severity thresholds and exported the detected events into a CSV file.

## Screenshots

Refer to the `Screenshots` folder for the project setup, execution steps, log analysis, and generated reports.

## Learning Outcomes

Through this project, I gained practical experience with:

- Linux command-line operations
- SSH authentication logs
- Python scripting for log analysis
- Regular expressions
- IP address tracking
- Security event classification
- CSV report generation
- Virtual machine-based cybersecurity labs

## Disclaimer

This project was developed for educational purposes in a controlled virtual lab environment. It is intended for learning and demonstrating basic SSH security log analysis. It is not a replacement for a production SIEM or enterprise security monitoring solution.
## Project Structure

ssh-log-detector/
│
├── Screenshots/
│
├── ssh_log_detector.py
├── ssh_log_detector_v2.py
├── ssh_log_detector.v3.py
├── ip_summary.txt
├── security_report.txt
├── security_report.csv
└── README.md

## Future Improvements

- Add real-time SSH log monitoring.
- Integrate email alerts for suspicious login activity.
- Add automatic IP blocking.
- Integrate with a SIEM platform such as Wazuh.