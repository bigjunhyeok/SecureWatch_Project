import re

# 의심스러운 로그 패턴 정규표현식 목록
SUSPICIOUS_PATTERNS = [
    re.compile(r"Failed password for invalid user"),     # 존재하지 않는 사용자로 로그인 실패
    re.compile(r"authentication failure"),               # 인증 실패 메시지
    re.compile(r"Invalid user .* from .*"),              # 잘못된 사용자 접근 시도 (IP 포함)
    re.compile(r"sudo: .* : command not found"),         # sudo 명령어 실패 (권한 남용 또는 오타)
]

# 로그 라인이 위 패턴 중 하나라도 매칭되면 True 반환
def is_suspicious(line: str) -> bool:
    return any(pattern.search(line) for pattern in SUSPICIOUS_PATTERNS)