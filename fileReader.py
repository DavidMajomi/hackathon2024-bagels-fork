
def read_Userfile(fileName):
    file_name = open(fileName,'r')
    file_contenet = file_name.readlines()
    file_name.close()
    print(file_contenet)

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
