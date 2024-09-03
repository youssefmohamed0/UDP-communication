import socket as sk
import random

ip = sk.gethostbyname(sk.gethostname())
port = 9090

PKG_NUM = 0

SERVER = sk.socket(sk.AF_INET,sk.SOCK_DGRAM)
SERVER.bind((ip,port))


while True:
    data, client_ip = SERVER.recvfrom(1024)
    print(f"received [{data.decode()}] from {client_ip} ")


    PKG_NUM = random.choice( [int(data.decode()), random.randint(int(data.decode())-5, int(data.decode())+4)] ) # simulate connection loss
    # PKG_NUM = int(data.decode())
    print(f"sending back [{PKG_NUM}] to {client_ip} ")

    SERVER.sendto(str(PKG_NUM).encode(),client_ip)

    print(f"______________________")