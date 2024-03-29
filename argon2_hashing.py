import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def get_user_passphrase():
    user_entered_passphrase = input("Enter the passphrase: ")
    user_entered_passphrase = bytes(user_entered_passphrase, 'utf-8')      # Converts passphrase to bytes

    salt = os.urandom(16)
    
    kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=480000,
    )
    
    hashed_passphrase = base64.urlsafe_b64encode(kdf.derive(user_entered_passphrase))
    print(hashed_passphrase)
    print("Hey")
    
    return hashed_passphrase
    
    
get_user_passphrase()