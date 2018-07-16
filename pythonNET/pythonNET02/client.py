# client.py
import socket
sk = socket.socket()
sk.connect(('127.0.0.1',8889))
while True:
    info = input('>>>')
    sk.send(bytes(info,encoding='utf-8'))
    ret = sk.recv(1024).decode('utf-8')
    print(ret)
    if ret == '##':
        sk.send(b'bye')
        break

sk.close()