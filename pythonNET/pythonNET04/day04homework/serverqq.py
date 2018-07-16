from socket import *
import os,sys

def do_login():
    print('登录')

def do_chat():
    print('聊天')

def do_quit():
    print('退出')



# 用来处理客户端请求
def do_child(s):
    while True:
        msg,addr = s.recvfrom(1024)
        msgList = msg.decode().split(' ')


        if msgList[0] == 'L':
            do_login()
        elif msgList[0] == 'C':
            do_chat()
        elif msgList[0] == 'Q':
            do_quit()


def do_parent():
    print('执行父进程')
    while True:
        pass


def main():
    # 服务端的地址
    ADDR = ('0.0.0.0',8888)
    # 创建套接字
    s = socket(AF_INET,SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)

    # 创建父子进程，分别处理请求和发送管理员消息
    pid = os.fork()

    if pid < 0:
        sys.exit('创建里程失败')
    elif pid == 0:
        #执行子进程功能
        do_child(s)
    else:
        #执行父进程的功能
        do_parent()



if __name__ == '__main__':
    main()

















