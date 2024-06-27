import socket
import sqlite3
import hashlib
import threading



server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost",9999))

server.listen()

def handle_connection(client):
    client.send("Username: ".encode())
    username = client.recv(1024).decode()
    client.send("Password: ".encode())
    password = client.recv(1024)
    password = hashlib.sha256(password).hexdigest()

    conn = sqlite3.connect("Userdata.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM Userdata WHERE username = ? AND password = ?",(username,password))
    if cur.fetchall():
        client.send("Login successful!".encode())
    else:
        client.send("Login failed!".encode())


while True:
    client,addr = server.accept()
    threading.Thread(target=handle_connection,args=(client,)).start()
    
