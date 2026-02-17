from cryptography.fernet import Fernet
from app.core.secrets import secrets_provider

def get_fernet():
    key = secrets_provider.get_secret("ENCRYPTION_KEY")
    return Fernet(key.encode())

def encrypt(value: str) -> str:
    f = get_fernet()
    return f.encrypt(value.encode()).decode()

def decrypt(value: str) -> str:
    f = get_fernet()
    return f.decrypt(value.encode()).decode()
