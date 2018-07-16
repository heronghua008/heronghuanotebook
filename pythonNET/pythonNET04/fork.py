import os

pid = os.fork()

if pid < 0:
    print("创建进程失败")
elif pid == 0:
    print('新创建的进程')
else:
    print("原来的进程")

print('程 序执行完毕')