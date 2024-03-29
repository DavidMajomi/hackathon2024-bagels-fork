import sqlite3

def add_data_to_db(username, password):
    conn_object = sqlite3.connect('database.db')
    
    cursor_obj = conn_object.cursor()
   
    table = """CREATE TABLE IF NOT EXISTS password_data(
                user_id INTEGER PRIMARY KEY,
                user_name TEXT,
                password TEXT);"""
                
    cursor_obj.execute(table)
    
    cursor_obj.execute(f'''INSERT INTO password_data (user_name, password) VALUES ('{username}', '{password}')''')
    
    conn_object.commit()
    conn_object.close
    
    
def test_data():
    add_data_to_db("name", "password")
    data = return_row_data()
    test_data = return_row_associated_with_user("test")
    
    # for row in data:
    #     print(row)
        
    # for lines in test_data:
    #     print(lines)
    test_data_passwords = parse_returned_passwords(test_data)
    
    for password in test_data_passwords:
        print(password)
        
    print(len(test_data))
    
    print("Done")
    
    
def return_row_data():
    
    conn_object = sqlite3.connect('database.db')
    cursor = conn_object.cursor()
    
    cursor_data = cursor.execute('''SELECT * FROM password_data''')
    
    conn_object.close
    
    return cursor_data
    
    
def return_row_associated_with_user(username):
    conn_object = sqlite3.connect('database.db')
    cursor = conn_object.cursor()
    
    
    cursor = conn_object.cursor()

    cursor.execute("SELECT * FROM password_data WHERE user_name = ?", (username,))

    rows = cursor.fetchall()
        
    # cursor_data = cursor.execute(f'''SELECT * FROM password_data WHERE name = "{username}"''')
    
    conn_object.close
    
    return rows
   
    
def parse_returned_passwords(row):
    passwords = []
    
    for values in row:
        password = values[2]
        passwords.append(password)
        
    return passwords
        
# test_data()
