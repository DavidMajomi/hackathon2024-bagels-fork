from cryptography.fernet import Fernet
from fernet_hashing import get_user_passphrase

passphrase = get_user_passphrase()
f = Fernet(passphrase)

def read_Userfile(fileName):
    file_name = open(fileName,'r')
    file_contenet = file_name.readlines()
    new_wrod = open("encode.txt","wb")
    
    allLines = ""
    for i in range(len(file_contenet)):
        allLines = allLines + file_contenet[i]
        
    token = f.encrypt(bytes(allLines, "utf-8"))
    new_wrod.write(token)
    
    new_wrod.close()


def decode_Userfile(fileName):
    file_name = open("encode.txt",'rb')
    file_contenet = file_name.readlines()
    str_line_with_hash = file_contenet[0]
    
    token = f.decrypt(str_line_with_hash)
    
    new_wrod = open(fileName,"w")
    new_wrod.write(token.decode())
    
    new_wrod.close()     


name = "test.txt"
read_Userfile(name)
decode_Userfile("decode.txt")
