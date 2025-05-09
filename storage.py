import os

# 감지된 로그 라인을 지정된 로그 파일에 저장하는 함수
def save_detected_log(line: str, file_path: str = "detected.log"):
    try:
        # 파일을 append 모드로 열고 UTF-8 인코딩 사용
        with open(file_path, "a", encoding="utf-8") as f:
            # 개행이 없으면 개행 추가해서 저장
            f.write(line if line.endswith("\n") else line + "\n")
    except Exception as e:
        # 파일 저장 중 오류 발생 시 에러 메시지 출력
        print(f"[ERROR] Failed to save log to {file_path}: {e}")