# from Crypto.cipher import AES
import argon2

def get_user_passphrase():
    user_entered_passphrase = input("Enter the passphrase: ")
    user_entered_passphrase = bytes(user_entered_passphrase, 'utf-8')
    hashed_passphrased = argon2.hash_password(user_entered_passphrase)
    print(hashed_passphrased)
    

get_user_passphrase()
