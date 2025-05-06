import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class LogHandler(FileSystemEventHandler):
    def __init__(self, file_path):
        self.file_path = os.path.abspath(file_path)  # ✅ 절대 경로로 변환
        self._position = os.path.getsize(self.file_path)  # 처음부터 읽지 않도록

    def on_modified(self, event):
        if os.path.abspath(event.src_path) == self.file_path:  # ✅ 비교도 절대경로로
            with open(self.file_path, 'r') as f:
                f.seek(self._position)
                new_lines = f.readlines()
                self._position = f.tell()
                for line in new_lines:
                    self.process_log(line)

    def process_log(self, line):
        print(f"[NEW LOG] {line.strip()}")


if __name__ == "__main__":
    log_file = "test.log"
    log_dir = os.path.dirname(os.path.abspath(log_file))  # ✅ 경로 정리

    event_handler = LogHandler(log_file)
    observer = Observer()
    observer.schedule(event_handler, path=log_dir, recursive=False)
    observer.start()

    print(f"✅ Watching {log_file} ... Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()