from cryptography.fernet import Fernet
from argon2_hashing import get_user_passphrase
def read_Userfile(fileName):
    file_name = open(fileName,'r')
    file_contenet = file_name.readlines()
    file_name.close()

    print(file_contenet)
    passphrase = get_user_passphrase()
    print(passphrase_64)
    for i in range(len(file_contenet)):
        f = Fernet(passphrase_64)

        message = file_contenet[i].strip("\n")
        token = f.encrypt(message)
        print(token)

name = "test.txt"
read_Userfile(name)

#import aes_cipher

#Pbkdf2Sha512Default = aes_cipher.Pbkdf2Sha512(512 * 1024)
#data = "asfdfasdggasdffasDas"
#hi=aes_cipher.DataEncrypter(Pbkdf2Sha512Default)
#hi.Encrypt(data,"test_pwd")

#print(hi.GetEncryptedData())


from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"A really secret message. Not for prying eyes.")

print(token)


with open(name, 'rb') as enc_file:
    encrypted_file = enc_file.read()
decrypted_file = fernet.decrypt(encrypted_file)

with open(name, "wb") as enc_file:
    dec_file.write(decrypted_file)

    