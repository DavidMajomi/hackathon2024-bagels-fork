from cryptography.fernet import Fernet
from fernet_hashing import get_user_passphrase
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


def decode_Userfile(fileName):
    file_name = open(fileName,'r')
    file_contenet = file_name.readlines()
    new_wrod = open("decode.txt","a+")
    for i in range(len(file_contenet)):
        token = f.decrypt(bytes(file_contenet[i],"utf-8"))
        new_wrod.write(str(token))

decode_Userfile("encode.txt")

    