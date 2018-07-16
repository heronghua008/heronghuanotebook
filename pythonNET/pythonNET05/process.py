import multiprocessing as mp
from time import sleep
a = 1
def fun():
    print('a=',a)
    sleep(3)
    print('子进程事件')


p = mp.Process(target=fun)


p.start()

sleep(2)
print('这是父进程')
while True:
    pass


# p.join()

fun()

print("-----------------------")