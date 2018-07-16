import multiprocessing as mp 
from time import sleep 
import os 

a = 1

#进程事件
def fun():
    # print("a = ",a)
    global a 
    a = 10000
    print(os.getpid())
    sleep(3)
    print("子进程事件")

#创建进程对象
p = mp.Process(target = fun)

#启动进程
p.start()

sleep(2)
print("这是父进程")



#回收进程
p.join()
while True:
    pass

print("===================")
# print(a)