import socket





def data_sender(username,password):
    """sends data to the server so it can be verified """
    client  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(("localhost",9999))


    message = client.recv(1024).decode()
    client.send(username.encode())

    message = client.recv(1024).decode()
    client.send(password.encode())

    msg = str(client.recv(1024).decode())

    return msg



