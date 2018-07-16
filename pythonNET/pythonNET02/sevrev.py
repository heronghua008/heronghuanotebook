# server.py
import socket
sk = socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen()
while True:
    conn,addr = sk.accept()
    print(conn.getpeername())
    print(addr)
    while True:
        ret = conn.recv(1024).decode()
        print(ret)
        if ret == '##':
            break
        info = input('>>>')
        conn.send(bytes(info,encoding='utf-8'))
    conn.close()
sk.close()
