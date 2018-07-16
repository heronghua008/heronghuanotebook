import os 

pid = os.fork()

if pid < 0:
    print("Create Process failed")
elif pid == 0:
    print("子进程ＰＩＤ",os.getpid())
    print("Parent PID",os.getppid())
else:
    print("父进程ＰＩＤ",os.getpid())
    print("Child PID",pid)