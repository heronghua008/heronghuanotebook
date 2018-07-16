import socket
sk = socket.socket()
sk.connect(('127.0.0.1',8899))
n = input('请输入路径：')

try:
    with open(n,"rb") as src:
        while True:
            b = src.read(1024)

            if not b:
                break
            sk.send(b)

except Exception:
    print("发送文件失败")
print('发送成功')
# ret = sk.recv(1024).decode('utf-8')
# print(ret)
sk.close()


