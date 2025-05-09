import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from storage import save_detected_log
from patterns import is_suspicious

class LogHandler(FileSystemEventHandler):
    def __init__(self, file_path):
        self.file_path = os.path.abspath(file_path)
        self._position = os.path.getsize(self.file_path)

    def on_modified(self, event):
        if os.path.abspath(event.src_path) == self.file_path:
            with open(self.file_path, 'r') as f:
                f.seek(self._position)
                new_lines = f.readlines()
                self._position = f.tell()
                for line in new_lines:
                    self.process_log(line)

    def process_log(self, line):
        print(f"[DEBUG] 검사 중: {line.strip()}")
        if is_suspicious(line):
            print(f"⚠️ [SUSPICIOUS] {line.strip()}")
            save_detected_log(line)
        else:
            print(f"[INFO] {line.strip()}")

if __name__ == "__main__":
    log_file = "test.log"
    log_dir = os.path.dirname(os.path.abspath(log_file))

    event_handler = LogHandler(log_file)
    observer = Observer()
    observer.schedule(event_handler, path=log_dir, recursive=False)
    observer.start()

    print(f"\u2705 Watching {log_file} ... Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()