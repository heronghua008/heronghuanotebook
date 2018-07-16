from socket import * 

s = socket()

#设置套接字选项 让端口立即释放
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

print(s.getsockopt(SOL_SOCKET,SO_REUSEADDR))

#文件描述符
print(s.fileno())
#套接字类型
print(s.type)
#地址族类型
print(s.family)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('176.47.9.83',8888))

#获取套接字绑定地址
print(s.getsockname())

s.listen(5)

connfd,addr = s.accept()

#获取connfd链接的客户端地址
print(connfd.getpeername())

data = connfd.recv(1024)
print(data)

s.close()