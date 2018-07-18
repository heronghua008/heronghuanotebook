from  multiprocessing import Event 

#创建事件对象
e = Event()

print(e.is_set())

e.set()   #设置事件

e.wait(5)
print("==================")
print(e.is_set())

e.clear() #清除设置
e.wait()