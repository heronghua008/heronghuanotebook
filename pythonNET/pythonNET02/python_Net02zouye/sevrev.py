import socket
sk = socket.socket()
sk.bind(('127.0.0.1',8899))
sk.listen()
conn,addr = sk.accept()
print(addr)
try:
    with open('heronghua.txt',"wb") as dst:
        while True:
            ret = conn.recv(1024)
            if not ret:
                break
            dst.write(ret)
except Exception:
    print('打开文件失败')
print('接受完成')
# conn.send('收到文件'.encode('utf-8'))
conn.close()
sk.close()