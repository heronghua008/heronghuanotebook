from socket import *
from time import sleep
# 设置广播地址
dest = ('176.47.9.255',9999)
s = socket(AF_INET,SOCK_DGRAM)
# 设置套接字可以发送接受广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
while True:
    sleep(1)
    n = input("请输入：")
    s.sendto(n.encode(),dest)

s.close()

