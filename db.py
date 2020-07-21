import sqlite3

def create_db():
    conn = sqlite3.connect("db")
    cursor = conn.cursor()
    with open("database.sql","r") as file:
        cursor.executescript(file.read())
    conn.close()
    
