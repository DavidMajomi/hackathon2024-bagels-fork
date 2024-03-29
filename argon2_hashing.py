# from Crypto.cipher import AES
import argon2

def get_user_passphrase():
    user_entered_passphrase = input("Enter the passphrase: ")
    user_entered_passphrase = bytes(user_entered_passphrase, 'utf-32')
    
    hashed_passphrase = argon2.hash_password(user_entered_passphrase)
    
    return hashed_passphrase

