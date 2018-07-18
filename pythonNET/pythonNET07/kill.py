import os 
import signal  

#给7264进程发送SIGKILL信号
os.kill(7264,signal.SIGKILL)