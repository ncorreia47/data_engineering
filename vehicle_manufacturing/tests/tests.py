from cryptography.fernet import Fernet
import os

print(f'Fernet key: {Fernet.generate_key().decode()}')
print(f'Webserver secret key: {os.urandom(24).hex()}')