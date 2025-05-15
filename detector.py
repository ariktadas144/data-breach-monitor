from alerts import send_alert
from datetime import datetime

def scan_logs(log_path="./sample_logs/auth.log"):
    print("[SCAN] Scanning for anomalies...")
    failed_count = 0
    ts_list = []

    with open(log_path, "r") as f:
        for line in f:
            if "Failed password" in line:
                failed_count += 1

                try:
                    parts = line.split()
                    date_str = "2025 " + " ".join(parts[0:3])
                    dt = datetime.strptime(date_str, "%Y %b %d %H:%M:%S")
                    ts_list.append(dt.strftime("%Y-%m-%d %H:%M:%S"))
                except Exception as e:
                    print(f"[WARN] Failed to parse timestamp: {e}")
                    continue

    print(f"[DEBUG] Failed attempts count: {failed_count}")

    if failed_count > 10:
        print("[ALERT] Unusual number of failed logins!")
        send_alert(f"Detected {failed_count} failed login attempts.")

        
        global failed_attempts
        failed_attempts = ts_list
    try:
        exec(open("visualizer.py").read(), {"failed_attempts": ts_list})
    except Exception as e:
        print(f"[VISUALIZER] Graph generation failed: {e}")

    else:
        print("[SCAN] No significant anomalies.")
