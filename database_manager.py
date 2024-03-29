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
    
    for row in data:
        print(row)
    
def return_row_data():
    
    conn_object = sqlite3.connect('database.db')
    cursor = conn_object.cursor()
    
    cursor_data = cursor.execute('''SELECT * FROM password_data''')
    
    conn_object.close
    
    return cursor_data
    
    
# test_data()
