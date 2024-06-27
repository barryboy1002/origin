import sqlite3
import hashlib

def create_user(username,password,email):
    """create the user and adds to existing database"""
    conn = sqlite3.connect("Userdata.db")
    cur = conn.cursor()
    cur.execute("""CREATE  TABLE IF NOT EXISTS Userdata(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT VARCHAR(255) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL ,
                email VARCHAR(255) NOT NULL ) """)
    #hash the password
    clean_password = hashlib.sha256(password.encode()).hexdigest()
    cur.execute ("""INSERT OR IGNORE INTO Userdata(username,password,email) VALUES(?,?,?)""",(username,clean_password,email))
    conn.commit()


