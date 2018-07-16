from multiprocessing import Process, Event
from time import sleep

'''
三个进程都要操作共享资源
要求必须主进程德操作
在子进程谁先操作都可以,但是有一个子进程不能长期阻塞

'''


def wait_event():
    print('想操作临界区,但是要等主进程操作完')
    e.wait()
    print('主进程操作完了,可以操作', e.is_set())


def wait_event_timeout(sec):
    print('也想操作临界区,但是也要等主进程操作完')
    e.wait(sec)
    print('等不了了,不等了造先执行别的', e.is_set())


e = Event()

p1 = Process(target=wait_event)
p2 = Process(target=wait_event_timeout, args=(2,))

p1.start()
p2.start()

print('主进程要先操作资源')
sleep(3)
print('主进程操作完毕')
e.set()

p1.join()
p2.join()