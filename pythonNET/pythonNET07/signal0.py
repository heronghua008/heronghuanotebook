import signal 
from time import sleep

signal.alarm(5)

#使用默认的方法处理SIGALRM信号
# signal.signal(signal.SIGALRM,signal.SIG_DFL)

#使用忽略的方法处理SIGALRM信号
signal.signal(signal.SIGALRM,signal.SIG_IGN)
#忽略ctrl+c 
signal.signal(signal.SIGINT,signal.SIG_IGN)

while True:
    sleep(2)
    print("让你恩ctrl + c")
    print("等待时钟...")