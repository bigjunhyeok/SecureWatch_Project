import re

# 의심스러운 로그 패턴 정규표현식 목록
SUSPICIOUS_PATTERNS = [
    re.compile(r"Failed password for invalid user"),
    re.compile(r"authentication failure"),
    re.compile(r"Invalid user .* from .*"),
    re.compile(r"sudo: .* : command not found"),
]

def is_suspicious(line: str) -> bool:
    return any(pattern.search(line) for pattern in SUSPICIOUS_PATTERNS)