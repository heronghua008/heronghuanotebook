from socket import *
from select import *

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('127.0.0.1',8889))
s.listen()


# 创建POLL对象
p = poll()

#建立通过fileno查找IO对象的字典
fdmap = {s.fileno():s}

# 注册关注IO事件
p.register(s,POLLIN | POLLERR)
while True:
    # 监控关注的IO
    events = p.poll()

    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print('Connect from',addr)
            p.register(c,POLLIN | POLLERR)
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


















