import argon2

def get_user_passphrase():
    user_entered_passphrase = input("Enter the passphrase: ")
    user_entered_passphrase = bytes(user_entered_passphrase, 'utf-8')      # Converts passphrase to bytes
    
    hashed_passphrase = argon2.hash_password(user_entered_passphrase)      # Encrypt passphrase using argon2
    # print(hashed_passphrase)
    
    return hashed_passphrase
    
    

get_user_passphrase()
