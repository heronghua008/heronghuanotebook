from multiprocessing import Process,Array 
import time 

#创建共享内存 列表是共享内存初始值
# shm = Array('i',[1,2,3,4,5])

#表示共享内存中开辟5个整形空间
shm = Array('i',5)

def fun():
    for i in shm:
        print(i)
    #修改共享内存内容
    shm[3] = 1000

p = Process(target = fun)
p.start()
p.join()
for i in shm:
    print(i)