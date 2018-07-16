from socket import *
# import socket
import os
sk = socket(AF_INET,SOCK_STREAM)
sk.bind(('localhost',9999))
sk.listen()
print('等待连接....')
conn,addr = sk.accept()
print('{}连接上'.format(addr))
ret = conn.recv(1024).decode()
print(ret)
data = os.popen(ret).read()
if len(data) == 0:
    data = '没有这个命令'
conn.send(str(len(data)).encode())
conn.send(data.encode())
print('传输结束')
conn.close()
sk.close()