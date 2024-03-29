#demo

# SP Char
#33 - 47
#58 - 64
#91 - 96
#123 - 126

#num
#48 - 57
usr = input()


#for i in range(len(usr)):
#    print(f"{usr[i]} = {ord(usr[i])}")

class ClassUser():
    def __init__(Username,Password):
        self.Username = Username
        self.Password = Password
        
    def password_Strenght_Validtion():
        spCha = 0
        upAphlCha = 0
        loAphlCha = 0
        print(len(self.Password))
        if (len(self.Password)<4) or (len(self.Password)>26):
            print("INVALID: Password is to long/shrot password should be in between 4 - 26 Characters")
        else:
            print("VALID: Password is in between 4 - 26 Characters")
            for i in range(len(self.Password)):
                if ((ord(self.Password[i])>=32) and (ord(self.Password[i])<=64)) or ((ord(self.Password[i])>=91) and (ord(self.Password[i])<=96)) or ((ord(self.Password[i])>=123) and (ord(self.Password[i])<=126)):
                    spCha +=1
                elif ((ord(self.Password[i])>=65) and (ord(self.Password[i])<=90)):
                    upAphlCha +=1
                else:
                    loAphlCha +=1

            if  (spCha < 2) or (spCha > 26):
                print("INVALID: Password as to many/little special Characters it should be in between 2 - 26 Characters.")
            else:
                print("VALID: Password special Characters are in between 2 - 26 Characters.")
            
            if (upAphlCha >=1) and (loAphlCha<=1):
                print("This password is strong.")
            else:
                print("INVALID: Password as to need at least one upper/lower Characters")


        
            
password_Strenght_Validtion(usr)