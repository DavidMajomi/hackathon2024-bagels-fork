from database_manager import return_row_associated_with_user, parse_returned_passwords
from demo import ClassUser
import os

def login():
    print(" Welcome to the login screen")
    
    valid = False
    number_of_user_tries = 0
    while((valid == False) and (number_of_user_tries <= 3)):
        # print("Enter a username:")
        
        user_name = input("Enter your user name: ")
        user_entered_password = input("Enter your password: ")
        
        value = ClassUser(user_name, user_entered_password) 
        valid = value.password_Strenght_Validtion()
        
        # if()
        
        user_data = return_row_associated_with_user(user_entered_password)
        passwords = parse_returned_passwords(user_data)
        
        for stored_password in passwords:
            if(user_entered_password == stored_password):
                valid = True
                os.system("cls")
                print(f"Welcome {user_name}")
            else:
                print('Invalid check your username and password')
                number_of_user_tries = number_of_user_tries + 1
                os.system("cls")
                
login()
        
        
        
        
        
        
    