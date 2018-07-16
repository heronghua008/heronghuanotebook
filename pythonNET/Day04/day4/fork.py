import os
from time import sleep 

#fork之前的部分只有父进程执行
print("======================")
a = 1

pid = os.fork()

if pid < 0:
    print("创建进程失败")
elif pid == 0:
    sleep(1)
    print("a = ",a)
    a = 10000
    print("新创建的进程")
else:
    sleep(2)
    print("原来的进程")
    print("parent a = ",a)

print("程序执行完毕") 