#demo

# SP Char
#33 - 47
#58 - 64
#91 - 96
#123 - 126


class ClassUser():
    def __init__(self, Username,Password):
        self.username = Username
        self.password = Password
        self.spCha = 0
        self.upAphlCha = 0
        self.loAphlCha = 0


    def get_upper(self):
        return self.upAphlCha
    
    def get_lower(self):
        return self.loAphlCha

    def getUsername(self):
        return self.username
    
    def getPassword(self):
        return self.password
    
    def password_Strenght_Validtion(self):
        
        if (len(self.password)<4) or (len(self.password)>26):
            print("INVALID: Password is to long/shrot password should be in between 4 - 26 Characters")
        else:
            print("VALID: Password is in between 4 - 26 Characters")
            for i in range(len(self.password)):
                if ((ord(self.password[i])>=32) and (ord(self.password[i])<=64)) or ((ord(self.password[i])>=91) and (ord(self.password[i])<=96)) or ((ord(self.password[i])>=123) and (ord(self.password[i])<=126)):
                    self.spCha +=1
                elif ((ord(self.password[i])>=65) and (ord(self.password[i])<=90)):
                    self.upAphlCha +=1
                elif((ord(self.password[i])>=87) and (ord(self.password[i])<=122)):
                    self.loAphlCha +=1

            if  (self.spCha < 2) or (self.spCha > 26):
                print("INVALID: Password as to many/little special Characters it should be in between 2 - 26 Characters.")
            else:
                print("VALID: Password special Characters are in between 2 - 26 Characters.")
            
            if (self.upAphlCha >=1) and (self.loAphlCha>=1):
                print("This password is strong.")
            else:
                print("INVALID: Password as to need at least one upper/lower Characters")

    
    def test_crack(self):

        
        #Mixed cases but no mixed characters
        #65 - 122
        if self.upAphlCha > 0 and self.loAphlCha > 0 and self.spCha == 0:
            return ((122-65)**len(self.password))/5 

        #No mixed cases just mixed_characters 
        #32 - 64
        elif self.upAphlCha > 0 and self.loAphlCha == 0 and self.spCha > 0:
            return ((64-32)**len(self.password))/5
        
        #No mixed cases just mixed_characters 
        #32 - 64
        elif self.upAphlCha == 0 and self.loAphlCha > 0 and self.spCha > 0:
            return ((64-32)**len(self.password))/5


        #No mixed cases just mixed_characters 
        #32 - 64
        elif self.spCha == 0:
            return ((64-32)**len(self.password))/5
        
        return (122**len(self.password))/5

    
#num
#48 - 57
print("Enter Username: ")
usr = input()

print("Enter Password")
pssw = input()


#for i in range(len(usr)):
#    print(f"{usr[i]} = {ord(usr[i])}")

user = ClassUser(usr, pssw)

user.password_Strenght_Validtion()

print(str(user.test_crack()) + " sec(s) to crack.")

