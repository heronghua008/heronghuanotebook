import socket
sk = socket.socket()
sk.connect(('localhost',9999))
ret = input('>>')
sk.send(ret.encode())
data_old = sk.recv(1024).decode()
print(data_old)
b = 0
c = b''
while b < int(data_old) :
    data = sk.recv(1024)
    c += data
    b += len(data.decode())
print(c.decode())
print(b)

sk.close()