import os 
from multiprocessing import Process
from time import sleep

size = os.path.getsize("./img.jpg")
#　如果在父进程打开则两个子进程操作同一个文件流
# fr = open('img.jpg','rb')

#复制上半部分
def copy1(filename):
    fr = open(filename,'rb')
    n = size // 2 
    fw = open('copy1.jpg','wb')

    while True:
        if n < 1024:
            data = fr.read(n)
            fw.write(data)
            break
        data = fr.read(1024)
        fw.write(data)
        n -= 1024
    fr.close()
    fw.close()

#复制下半部分
def copy2(filename):
    fr = open(filename,'rb')
    fw = open('copy2.jpg','wb')
    fr.seek(size // 2,0)  #文件偏移位置到中间

    while True:
        data = fr.read(1024)
        if not data:
            break 
        fw.write(data)
    fw.close()
    fr.close()

p1 = Process(target = copy1,args = ("img.jpg",))
p2 = Process(target = copy2,args = ("img.jpg",))

p2.start()
sleep(0.5)
p1.start()


p1.join()
p2.join()
