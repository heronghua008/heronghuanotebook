import os 
from multiprocessing import Process 

#获取文件大小
size = os.path.getsize("./file.jpg")
#两个子进程操作同一个文件流会产生错乱
# f = open('file.jpg','rb')

#复制前半部分
def copy1(filename):
    f = open(filename,'rb')
    n = size // 2
    fw = open('copy1.jpg','wb')

    while True:
        if n < 128:
            data = f.read(n)
            fw.write(data)
            break
        data = f.read(128)
        fw.write(data)
        n -= 128
    f.close()
    fw.close() 

#复制下半部分
def copy2(filename):
    f = open(filename,'rb')
    fw = open('copy2.jpg','wb')
    f.seek(size // 2,0)
    while True:
        data = f.read(128)
        if not data:
            break 
        fw.write(data)
    fw.close()
    f.close()

p1 = Process(target = copy1,args = ("file.jpg",))
p2 = Process(target = copy2,args = ("file.jpg",))

p1.start()
p2.start()

p1.join()
p2.join()