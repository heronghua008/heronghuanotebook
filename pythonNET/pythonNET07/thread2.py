from threading import Thread,currentThread 
from time  import sleep  

#线程函数
def fun(sec):
    print("线程属性测试")
    sleep(sec)
    #通过线程对象getName()函数得到线程名称
    print("%s 线程结束"%currentThread().getName())

#线程对象列表
thread = []
for i in range(3):
    t = Thread(name = 'tedu' + str(i),\
        target = fun,args = (3,))
    thread.append(t)
    t.start()
    print(t.is_alive()) #线程状态

thread[1].setName("Tarena") #设置线程名称
print(thread[2].name) #获取线程名字

#回收线程
for i in thread:
    i.join()
