import hashlib


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(password: str, hashed_password :str) -> str:
    return hashlib.sha256(password.encode()).hexdigest() == hashed_password