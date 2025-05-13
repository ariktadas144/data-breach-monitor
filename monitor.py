import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class LogHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".log"):
            print(f"[MONITOR] Detected change: {event.src_path}")
            # Optionally call detector logic here

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
