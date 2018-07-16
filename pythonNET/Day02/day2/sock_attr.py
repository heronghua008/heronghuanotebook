from socket import *

s = socket()

#获取套接字类型
print(s.type)
#获取地址族类型
print(s.family)

#获取文件描述符
print(s.fileno())

#设置端口可重用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

#获取选项值
print(s.getsockopt(SOL_SOCKET,SO_REUSEADDR))

s.bind(('172.60.50.93',8888))

#获取绑定地址
print(s.getsockname())

s.listen(5)

c,addr = s.accept()
#获取链接端地址
print(c.getpeername())

data = c.recv(1024)
print(data)

c.close()
s.close()
