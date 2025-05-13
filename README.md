# Data Breach Detector

A Python-based command-line tool for early detection of suspicious activity in system logs - such as brute-force login attempts - to help identify potential data breaches as they happen.

---

## Features

- Real-time log monitoring using the `watchdog` library
- Detection of suspicious patterns (e.g., multiple failed login attempts)
- Support for custom log files (`auth.log` simulated)
- Modular alert system (currently prints to console, easily extendable)
- Easily customizable detection thresholds and logic

---

## 🛠Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/data-breach-detector.git
   cd data-breach-detector
   ```

2. **Install Dependencies**

   Make sure Python 3.x is installed. Then install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` doesn't exist, just install `watchdog`:

   ```bash
   pip install watchdog
   ```

---

## Project Structure

```
data_breach_detector/
├── cli.py             # Command-line interface
├── monitor.py         # Real-time log file watcher
├── detector.py        # Breach detection logic
├── alert.py           # Alerting system (prints or sends alerts)
├── sample_logs/
│   └── auth.log       # Sample log file to simulate attacks
```

## Usage

1. **Start Real-Time Monitoring**

   ```bash
   python cli.py monitor
   ```

   Watches `sample_logs/auth.log` and automatically scans for anomalies on any file change.

2. **Run One-Time Scan**

   ```bash
   python cli.py scan
   ```

   Scans the current log file for potential data breach indicators (e.g., brute-force attempts).

3. **Trigger a Manual Alert (Test)**

   ```bash
   python cli.py alert
   ```

   Sends a manual test alert.

---

## Simulating a Breach

- Open `sample_logs/auth.log` in a text editor.
- Add 10+ lines simulating failed login attempts, for example:

  ```
  May 13 10:01:00 server sshd[1234]: Failed password for invalid user admin from 192.168.1.101
  ```

- Save the file.
- The monitor will detect the change and scan it.

---

## Configuration

- **Thresholds:** Detection logic in `detector.py` can be adjusted for different log formats or threshold sensitivity.
- **Alerting:** `alert.py` can be extended to send alerts via email (`smtplib`), Slack, Telegram, or Discord.

---

## To-Do / Future Features

- Email/Discord/Slack notifications
- Configurable alert thresholds via CLI or config file
- Dashboard with breach activity timeline
- Integration with system logs on Linux (`/var/log/auth.log`)

---
