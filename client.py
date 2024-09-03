import socket as sk
import time

ip = sk.gethostbyname(sk.gethostname())
port = 9090

PKG_NUM = 0

sock = sk.socket(sk.AF_INET,sk.SOCK_DGRAM)

while True:

    sock.sendto(str(PKG_NUM).encode(),(ip,port))
    print(f"sent to server: [{PKG_NUM}]")
    try :
        data, server_address = sock.recvfrom(1024)
    except:     # exception in case server is dosconnected
        print("no response from server, re-requesting packet\n______________________")
        time.sleep(3)
        continue
    print(f"recived from server : [{data.decode()}]")

    if data.decode() != str(PKG_NUM):   # check if response is same as message
        print(f"wrong packet, re-requesting packet\n______________________")
        time.sleep(3)
        continue

    print(f"packet sent succefully\n______________________")
    PKG_NUM+=1
    

    time.sleep(3)