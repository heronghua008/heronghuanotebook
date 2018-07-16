from socket import *
from select import *

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('127.0.0.1',8889))
s.listen()


# 创建EPOLL对象
p = epoll()

#建立通过fileno查找IO对象的字典
fdmap = {s.fileno():s}

# 注册关注IO事件
p.register(s,EPOLLIN | EPOLLERR)
while True:
    # 监控关注的IO
    events = p.poll()

    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print('Connect from',addr)
            注册关注IO事件
            p.register(c,EPOLLIN | EPOLLERR)
            fdmap[c.fileno()] = c
        elif event & POLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]

            else:
                print(data.decode())
                fdmap[fd].send('收到了'.encode())


















