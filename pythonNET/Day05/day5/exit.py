import os 
import sys 

#进程结束
# os._exit(0)

try:
    sys.exit("进程退出")
except SystemExit as e:
    print(e)

print("Process end")