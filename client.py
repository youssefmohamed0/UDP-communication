import socket as sk
import time

ip = sk.gethostbyname(sk.gethostname())
port = 9090

PKG_NUM = 0



while True:
    sock = sk.socket(sk.AF_INET,sk.SOCK_STREAM)
    sock.connect((ip,port))

    sock.send(str(PKG_NUM).encode())
    data = sock.recv(1024)
    print(f"recived from server: {data.decode()}")
    PKG_NUM+=1
    
    sock.detach()

    time.sleep(0.5)