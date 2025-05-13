import argparse
from monitor import start_monitoring
from detector import scan_logs
from alerts import send_alert

def main():
    parser = argparse.ArgumentParser(description="Early Data Breach Detection CLI Tool")
    parser.add_argument("command", choices=["monitor", "scan", "alert"], help="Command to run")

    args = parser.parse_args()

    if args.command == "monitor":
        start_monitoring()
    elif args.command == "scan":
        scan_logs()
    elif args.command == "alert":
        send_alert("Manual breach alert test.")

if __name__ == "__main__":
    main()
