# 二分查找算法 必须处理有序的列表
l = [2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]
n = 0
def find(n,l,aim,start = 0,end = None):
    n += 1
    print(n)
    end = len(l) if end is None else end
    mid_index = (end - start)//2 + start
    if start <= end:
        if l[mid_index] < aim:
            return find(n,l,aim,start =mid_index+1,end=end)
        elif l[mid_index] > aim:
            return find(n,l, aim, start=start, end=mid_index-1)
        else:
            return mid_index
    else:
        return '找不到这个值'

ret= find(n,l,67)
print(ret)
print('蒋康雷是个GAY')

from urllib import request


list
tuple