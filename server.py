import socket as sk

ip = sk.gethostbyname(sk.gethostname())
port = 9090

PKG_NUM = 0

SERVER = sk.socket(sk.AF_INET,sk.SOCK_STREAM)

SERVER.bind((ip,port))

SERVER.listen(5)

while True:
    client_sock, client_ip = SERVER.accept() # establishes connection
    print(f"connection with {client_ip} started")
    # client sock is used to talk to client
    data = client_sock.recv(1024)   # recieves data with byte size 1024
    PKG_NUM = int(data.decode())
    print(f"[{data.decode()}] obtained from {client_ip}:")
    client_sock.send(str(PKG_NUM).encode())
    client_sock.close()
    print(f"connection with {client_ip} ended")