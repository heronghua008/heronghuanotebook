from socket import *
s = socket()
s.bind(('127.0.0.1',8889))
s.listen(5)

c,addr = s.accept()
print('Connect from',addr)
f = open('herong.png','wb')
while True:
    data = c.recv(1024)
    f.write(data)
    if not data:
        break
f.close()
c.close()
s.close()