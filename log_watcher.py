import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from storage import save_detected_log      # 감지된 로그를 파일에 저장하는 함수
from patterns import is_suspicious         # 로그가 의심스러운지 판단하는 함수

# 로그 변경 이벤트를 처리하는 클래스
class LogHandler(FileSystemEventHandler):
    def __init__(self, file_path):
        # 감시할 로그 파일의 절대 경로
        self.file_path = os.path.abspath(file_path)
        # 현재 파일 크기 위치 저장 (이후부터 읽기 위함)
        self._position = os.path.getsize(self.file_path)

    def on_modified(self, event):
        # 변경된 파일이 감시 대상 파일일 경우에만 처리
        if os.path.abspath(event.src_path) == self.file_path:
            with open(self.file_path, 'r') as f:
                # 마지막 읽은 위치부터 새 로그를 읽어옴
                f.seek(self._position)
                new_lines = f.readlines()
                self._position = f.tell()

                # 새 로그 라인을 하나씩 처리
                for line in new_lines:
                    self.process_log(line)

    def process_log(self, line):
        print(f"[DEBUG] 검사 중: {line.strip()}")
        if is_suspicious(line):
            # 의심 로그인 경우 콘솔 출력 및 파일 저장
            print(f"⚠️ [SUSPICIOUS] {line.strip()}")
            save_detected_log(line)
        else:
            # 일반 정보 로그는 정보용 출력만
            print(f"[INFO] {line.strip()}")

# 프로그램 시작 지점
if __name__ == "__main__":
    log_file = "test.log"  # 감시할 로그 파일 이름
    log_dir = os.path.dirname(os.path.abspath(log_file))  # 디렉토리 경로 추출

    # 이벤트 핸들러 및 감시자 객체 생성
    event_handler = LogHandler(log_file)
    observer = Observer()
    observer.schedule(event_handler, path=log_dir, recursive=False)
    observer.start()

    print(f"✅ Watching {log_file} ... Press Ctrl+C to stop.")

    # Ctrl+C가 눌릴 때까지 감시 유지
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()