#tcp_server.py 
from socket import *  

#创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)

#绑定地址
sockfd.bind(('172.60.50.50',9999))

#设置监听
sockfd.listen(5)
while True:
    print("Waiting for connect....")
    connfd,addr = sockfd.accept()
    print("Connect from",addr)
    while  True:
        data = connfd.recv(5)
        if not data:
            break
        print("Receive message:",data.decode())
        connfd.send(b'I love China')
    connfd.close()

sockfd.close()


