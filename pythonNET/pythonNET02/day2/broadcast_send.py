#broadcast_send.py
from socket import *
from time import sleep 

#广播地址 <broadcast>
dest = ('172.60.50.255',9999)

s = socket(AF_INET,SOCK_DGRAM)

#设置套接字可以发送接收广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

while True:
    sleep(2)
    s.sendto("加油，比利时!!".encode(),dest)

s.close()



