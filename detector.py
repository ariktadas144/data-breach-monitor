def scan_logs(log_path="./sample_logs/auth.log"):
    print("[SCAN] Scanning for anomalies...")
    failed_attempts = 0
    with open(log_path, "r") as f:
        for line in f:
            if "Failed password" in line:
                failed_attempts += 1
    if failed_attempts > 10:
        print("[ALERT] Unusual number of failed logins!")
        from alert import send_alert
        send_alert(f"Detected {failed_attempts} failed login attempts.")
    else:
        print("[SCAN] No significant anomalies.")
