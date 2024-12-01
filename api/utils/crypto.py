from cryptography.fernet import Fernet
from api.config.settings import settings


encryption_key = Fernet.generate_key(
) if not settings.secret_key else settings.secret_key.encode()
cipher = Fernet(encryption_key)


def encrypt_data(data: str) -> str:
    encrypted_data = cipher.encrypt(data.encode('utf-8'))
    return encrypted_data.decode('utf-8')


def decrypt_data(encrypted_data: str) -> str:
    decrypted_data = cipher.decrypt(encrypted_data.encode('utf-8'))
    return decrypted_data.decode('utf-8')
