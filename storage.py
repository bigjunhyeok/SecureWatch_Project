import os

def save_detected_log(line: str, file_path: str = "detected.log"):
    try:
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(line if line.endswith("\n") else line + "\n")
    except Exception as e:
        print(f"[ERROR] Failed to save log to {file_path}: {e}")