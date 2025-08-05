import re

def validate_password(password: str) -> str:
    if len(password) < 12:
        return PasswordStrength.WEAK
    if not re.search(r'[A-Z]', password):
        return PasswordStrength.WEAK
    if not re.search(r'[a-z]', password):
        return PasswordStrength.WEAK
    if not re.search(r'\d', password):
        return PasswordStrength.WEAK
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return PasswordStrength.MODERATE
    return PasswordStrength.STRONG

