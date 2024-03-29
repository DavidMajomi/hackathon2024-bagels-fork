import argon2

def get_user_passphrase():
    user_entered_passphrase = input("Enter the passphrase: ")
<<<<<<< HEAD
    user_entered_passphrase = bytes(user_entered_passphrase, 'utf-32')
    
    hashed_passphrase = argon2.hash_password(user_entered_passphrase)
=======
    user_entered_passphrase = bytes(user_entered_passphrase, 'utf-8')      # Converts passphrase to bytes
    
    hashed_passphrase = argon2.hash_password(user_entered_passphrase)      # Encrypt passphrase using argon2
    # print(hashed_passphrase)
>>>>>>> 5ca62c314beb6c50691a6ade549952f94fae1a5c
    
    return hashed_passphrase

