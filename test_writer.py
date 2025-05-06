import time

log_path = "test.log"
i = 0

while True:
    with open(log_path, "a") as f:
        f.write(f"May 7 11:{i:02}:00 test sshd[1111]: Failed password for root from 192.168.0.{i%255} port 22 ssh2\n")
    print(f"[WRITE] log line {i+1} added")
    i += 1
    time.sleep(2)  # 2초마다 1줄씩 쓰기