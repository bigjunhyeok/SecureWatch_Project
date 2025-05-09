import time
import random

# 로그를 쓸 파일 경로
log_file = "test.log"

# 감지되도록 설계된 의심스러운 로그 메시지 목록
suspicious_logs = [
    "Failed password for invalid user test from 10.0.0.3 port 22 ssh2",  # 로그인 실패
    "authentication failure for user root",  # 인증 실패
    "Invalid user admin from 192.168.1.1"  # 존재하지 않는 사용자 접근
]

# 무한 반복으로 주기적으로 로그를 생성
while True:
    with open(log_file, "a") as f:
        # 목록 중 랜덤으로 한 줄 선택
        line = random.choice(suspicious_logs)
        # 로그 파일에 기록
        f.write(line + "\n")
        # 콘솔에도 출력
        print(f"[WRITE] {line}")

    # 다음 로그 쓰기까지 대기 (3초)
    time.sleep(3)