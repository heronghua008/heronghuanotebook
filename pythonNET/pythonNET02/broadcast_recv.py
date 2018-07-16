from socket import *
# 创建套接字
s = socket(AF_INET,SOCK_DGRAM)

# 设置可以接收广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

# 绑定关口
s.bind(('176.47.9.83',9999))
while True:
    try:
        msg,addr = s.recvfrom(1024)
        print('从{}获取信息：{}'.format(addr,msg.decode()))
    except KeyboardInterrupt:
        print('接收消息结束')
        break
    except Exception as e:
        print(e)
s.close()