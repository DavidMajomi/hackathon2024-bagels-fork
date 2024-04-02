from cryptography.fernet import Fernet
from argon2_hashing import get_user_passphrase
passphrase = get_user_passphrase()
f = Fernet(passphrase)
def read_Userfile(fileName):
    file_name = open(fileName,'r')
    file_contenet = file_name.readlines()
    new_wrod = open("encode.txt","a+")
    for i in range(len(file_contenet)):
        token = f.encrypt(bytes(file_contenet[i],"utf-8"))
        new_wrod.write(str(token))


name = "test.txt"
read_Userfile(name)

#import aes_cipher

#Pbkdf2Sha512Default = aes_cipher.Pbkdf2Sha512(512 * 1024)
#data = "asfdfasdggasdffasDas"
#hi=aes_cipher.DataEncrypter(Pbkdf2Sha512Default)
#hi.Encrypt(data,"test_pwd")

#print(hi.GetEncryptedData())


def decode_Userfile(fileName):
    file_name = open(fileName,'r')
    file_contenet = file_name.readlines()
    new_wrod = open("decode.txt","a+")
    for i in range(len(file_contenet)):
        token = f.decrypt(bytes(file_contenet[i],"utf-8"))
        new_wrod.write(str(token))

decode_Userfile("encode.txt")

    