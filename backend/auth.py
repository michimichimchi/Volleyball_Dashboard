from pwdlib import PasswordHash

ph = PasswordHash.recommended()

def get_password_hash(plain_password: str) -> str:
# creates argon2 hash with salt already in it
    return ph.hash(plain_password)