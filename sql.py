import mysql.connector
conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='992992'  
    )
    
if conn.is_connected():
        print("Connection established")


