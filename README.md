# SecureWatch_Project

**SecureWatch**는 리눅스 시스템 로그를 실시간으로 감시하고, 의심스러운 활동을 탐지하여 기록하는 보안 로그 모니터링 툴입니다. `watchdog`을 활용하여 로그 파일 변경을 감지하며, 정규표현식을 통해 이상 징후를 분석합니다.

---

## 📁 프로젝트 구성

```
SecureWatch_Project/
├── log_watcher.py       # 실시간 로그 감시 메인 스크립트
├── patterns.py          # 의심 로그 정규표현식 정의
├── storage.py           # 감지된 로그를 파일에 저장
├── test_writer.py       # 테스트용 로그 생성기
├── test.log             # 감시 대상 로그 파일
├── detected.log         # 탐지된 로그 기록 파일 (자동 생성)
└── README.md            # 프로젝트 설명 파일
```

---

## ✅ 주요 기능

- 실시간 로그 파일 변경 감지 (`watchdog` 기반)
- 수상한 로그 패턴 탐지 (정규표현식)
- 탐지된 로그를 `detected.log`에 저장
- 테스트용 로그 자동 생성 기능 포함

---

## 🚀 사용 방법

### 1. 의존성 설치
```bash
pip install watchdog
```

### 2. 로그 감시 실행
```bash
python log_watcher.py
```

### 3. 테스트 로그 생성 (다른 터미널에서 실행)
```bash
python test_writer.py
```

> `test_writer.py`는 `test.log`에 수상 로그를 자동으로 추가해 `log_watcher.py`의 동작을 테스트합니다.

---

## ⚙️ 커스터마이징

- `patterns.py` : 감지 기준이 되는 정규표현식 수정 가능
- `log_file` 경로 : `log_watcher.py`에서 `log_file = "test.log"` 부분 수정 가능
- 저장 파일명 : `storage.py`의 기본 파일명을 수정 가능

---

## 📄 예시 로그
```
Failed password for invalid user test from 10.0.0.3 port 22 ssh2
authentication failure for user root
Invalid user admin from 192.168.1.1
```

---

## 📌 기타

- `.gitignore`에 `*.log`, `__pycache__/`, `.idea/` 등이 포함되어야 합니다.
- 테스트 로그는 수초 간격으로 무한 생성되므로, 수동으로 종료(Ctrl+C)하세요.

---

## 🛡️ 개발 목적

보안 로그 모니터링을 통해 시스템 침입 징후를 빠르게 포착하고, 대응 속도를 높이기 위한 실습형 프로젝트입니다.