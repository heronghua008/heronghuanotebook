from socket import *
from  select import select
import sys
#创建tcp套接字作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('127.0.0.1',8889))
s.listen(5)


# 三个关注列表
rlist = [s]
wlist = []
xlist = [s]

while True:
    # 提交关注的IO事件，等待处理
    print('waiting for IO...')
    rs,ws,xs = select(rlist,wlist,xlist)
    print(len(rs))
    for r in rs:
        if r is s:
            connfd,addr = r.accept()
            print('connect from',addr)
            # 增加关注事件
            rlist.append(connfd)
        else:
            data = r.recv(1024).decode()

            if not data:
                rlist.remove(r)
                r.close()
            print('Receive:',data)
            # 加入到要处理的IO事件列表
            wlist.append(r)
            # r.send(b'Receive your message')
    for w in ws:
        w.send('这是一条回复消息'.encode())
        wlist.remove(w)

    # 处理发生异常
    for x in xs:
        if x is s:
            s.close()
            sys.exit(0)





