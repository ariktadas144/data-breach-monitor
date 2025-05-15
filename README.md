# Data Breach Detector

A Python-based command-line tool for early detection of suspicious activity in system logs - such as brute-force login attempts - to help identify potential data breaches as they happen.

---

## Features

- Real-time log monitoring using the `watchdog` library  
- Automatic detection of suspicious patterns (e.g., multiple failed login attempts)  
- Scans simulated or real system log files (`auth.log`)  
- Generates a graph showing failed login frequency over time  
- Sends email alerts with the graph image attached  
- Modular architecture for alerts, detection logic, and future integrations  
- Customizable detection thresholds and log patterns  

---

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/data-breach-detector.git
   cd data-breach-detector
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` is missing, install manually:

   ```bash
   pip install watchdog matplotlib
   ```

---

## Project Structure

```
data_breach_detector/
├── cli.py               # Command-line interface
├── monitor.py           # Real-time log monitoring using watchdog
├── detector.py          # Log analysis and anomaly detection
├── alerts.py            # Sends alerts via console + email (with graph)
├── visualizer.py        # Graphs failed login attempts with matplotlib
├── sample_logs/
│   └── auth.log         # Simulated log file
├── failed_attempts_plot.png  # Generated graph (auto-created)
```

---

## Configuration

Edit `alerts.py` and set your SMTP details directly:

```python
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"
RECIPIENT_EMAIL = "recipient_email@gmail.com"
```

For Gmail users: enable 2FA and use an App Password.

---

## Usage

1. **Start Real-Time Monitoring**

   ```bash
   python cli.py monitor
   ```

   This watches the `sample_logs/auth.log` file and scans automatically when modified.

2. **Run a Manual Scan**

   ```bash
   python cli.py scan
   ```

   Scans the current log file, generates a graph, and sends an alert email if a breach is detected.

3. **Trigger a Manual Test Alert**

   ```bash
   python cli.py alert
   ```

   Sends a test alert (console + email without graph).

---

## Simulating a Breach

Open `sample_logs/auth.log` in a text editor.

Add 11 or more lines like:

```
May 13 10:01:00 server sshd[1234]: Failed password for invalid user admin from 192.168.1.101
```

Save the file.

If monitoring is running, it will detect and alert immediately.

---

## Graph Example

When a breach is detected:

- A line chart is generated showing login attempt frequency  
- The chart is saved as `failed_attempts_plot.png`  
- This image is attached to the email alert  

---

## To-Do / Future Enhancements

- Embed chart in email body (HTML email)  
- CLI-configurable thresholds and paths  
- Integration with Slack, Discord, or Telegram for real-time alerts  
- Web dashboard (Flask/React) to view live log and alerts  
- Syslog and `/var/log/auth.log` support for production Linux systems  

---
