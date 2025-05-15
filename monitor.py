import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from detector import scan_logs

class LogHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_processed = 0
        self.cooldown_seconds = 1  # Ignore duplicate events within 1 second

    def on_modified(self, event):
        if event.src_path.endswith(".log"):
            now = time.time()
            if now - self.last_processed > self.cooldown_seconds:
                print(f"[MONITOR] Detected change: {event.src_path}")
                scan_logs(event.src_path)
                self.last_processed = now

def start_monitoring(path="./sample_logs"):
    print("[MONITOR] Starting log monitoring...")
    event_handler = LogHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
