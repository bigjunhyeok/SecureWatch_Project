import time
import random

log_file = "test.log"
suspicious_logs = [
    "Failed password for invalid user test from 10.0.0.3 port 22 ssh2",
    "authentication failure for user root",
    "Invalid user admin from 192.168.1.1"
]

while True:
    with open(log_file, "a") as f:
        line = random.choice(suspicious_logs)
        f.write(line + "\n")
        print(f"[WRITE] {line}")
    time.sleep(3)  # 3초마다 로그 생성