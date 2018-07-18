from xs_cd import zhucaidan
from student_info import *


def xueshenglxt():#
    while True:
        zhucaidan()
        n = input("请输入您要查询的选项按q可以退出程序：")
        if n == "1":
            input_student()
        elif n =="2":
            output_student(L)
        elif n == "3":
            shanchuxingxi()
        elif n == "4":
            xiugaixingxing()
        elif n == "5":
            output_student(sorted(L, key=lambda x:x["score"],reverse=True))
        elif n == "6":
            output_student(sorted(L, key=lambda x:x["score"]))
        elif n == "7":
            output_student(sorted(L, key=lambda x:x['age'],reverse=True))
        elif n == "8":
            output_student(sorted(L, key=lambda x:x['age']))
        elif n == "9":
            baocuixinxi()
        elif n == "10":
            read_file_content()
        elif n == "q":
            print("程序结束")
            break
        else:
            print("您输入错误，请重新输入")
if __name__=='__main__':
    xueshenglxt()