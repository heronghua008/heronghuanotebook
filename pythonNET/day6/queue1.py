from multiprocessing import Queue 
from time import sleep

#创建队列
q = Queue(3)

q.put(1)
sleep(1)
print(q.empty())
# print(q.full())
# q.put(2)
# q.put(3)
# print(q.full())

# # q.put(4,True,3)
# print(q.get())
# print(q.qsize()) #查看消息数量
# print(q.empty())
# q.close()