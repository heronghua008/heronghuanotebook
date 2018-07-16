import signal
import time


signal.alarm(3)

while True:
    time.sleep(1)
    print("等待时钟信号....")