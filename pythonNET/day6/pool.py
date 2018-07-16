from multiprocessing import Pool 
from time import sleep,ctime 

def worker(msg):
    sleep(2)
    print(msg)
    return ctime()

#创建进程池对象
pool = Pool(processes = 4)

result = []
for i in range(10):
    msg = "hello %d"%i 
    #将事件加入到进程池
    pool.apply(func = worker,args = (msg,))
    # r = pool.apply_async(func = worker,args = (msg,))
    # result.append(r)

#关闭进程池
pool.close()
#回收进程
pool.join()

#打印各个事件函数返回值
# for i in result:
#     print(i.get())