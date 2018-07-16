from socket import *
from time import sleep,ctime
s = socket()
s.bind(('127.0.0.1', 8889))
s.listen(5)
# 设置超时等待时间
s.settimeout(5)

while True:
    print('Waiting for connect...')
    try:
        connfd,addr = s.accept()
    except timeout:
        print("time out...")
        sleep(2)
        print(ctime())
        continue
    print('Connect from',addr)
    connfd.settimeout(5)
    while True:
        data = connfd.recv(1024).decode()
        if not data:
            break
        print(data)
        connfd.sendall(ctime().encode())
    connfd.close()
s.close()