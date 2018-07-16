import os,sys 
from time import sleep


pid = os.fork()

if pid < 0:
    print("create process failed")
elif pid == 0:
    sleep(3)
    print("子进程ＰＩＤ:",os.getpid())
    sys.exit(3)
else: 
    #等待子进程退出
    while True:
        sleep(1)
        pid,status = os.waitpid(-1,os.WNOHANG)
        print(pid,status)
        if os.WEXITSTATUS(status):
            break
        print("do something others")
    while True:
        pass  