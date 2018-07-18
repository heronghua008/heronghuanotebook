
from student import Student
L = []
def input_student():  # 此函数添加学行信息
    while True:
        z = {}
        n = input('请输入姓名：')
        if n == "":
            break
        a = int(input('请输入年龄：'))
        s = int(input('请输入成绩：'))
        z = Student(n,a,s)
        L.append(z.__dict__)


'''----------------------------------------------------------------------------------------'''


def output_student(L):  # 此函数为查询信息
    a = "+" + "-" * 13 + "+" + "-" * 10 + "+" + "-" * 10 + "+"
    print(a)
    print("|" + "name".center(13) + "|" + "age"
          .center(10) + "|" + "score".center(10) + "|")
    print(a)
    for i in L:
        print("|" + i["name"].center(13) +
              "|" + str(i["age"]).center(10) +
              "|" + str(i["score"]).center(10) + "|")
    print(a)


'''----------------------------------------------------------------------------------------'''


def shanchuxingxi():  # 此函数为删除学生信息
    while True:
        n = input("请输入学生名字,按q可以返回到主菜单：")
        if n == "q":
            break
        for i in L:
            if i["name"] == n:
                L.remove(i)


'''----------------------------------------------------------------------------------------'''


def xiugaixingxing():  # 此函数为修改学生成绩
    while True:
        n = input("请输入学生名字,按q可以返回到主菜单：")
        if n == "q":
            break
        for i in L:
            if i["name"] == n:
                i["score"] = int(input("请输入要修改的分数："))


'''--------------------------------此处是5到8的功能---------------------------------------------'''
# def score_sort(x):
#     return x["score"] # x["score"]用来绑定列表L中每个字典键对应的值
# def age_sort(x):
#     return x["age"]
'''--------------------------------此处是9的功能---------------------------------------------'''


def baocuixinxi():
    f = open('si.txt', 'wb')
    for i in L:
        f.write(i["name"].encode("utf-8"))
        f.write(" ".encode("utf-8"))
        f.write(str(i['age']).encode("utf-8"))
        f.write(" ".encode("utf-8"))
        f.write(str(i["score"]).encode("utf-8"))
        f.write("\n".encode("utf-8"))
    f.close()


'''--------------------------------此处是10的功能---------------------------------------------'''


def read_file_content():
    L1 = []
    f = open("si.txt")
    while True:
        s = f.readline()
        if not s:
            break
        s2 = s.strip()
        name_age_score = s2.split()
        n, a, s = name_age_score
        d = {'name': n, 'age': int(a), 'score': s}
        L1.append(d)
    f.close()
    for i in L1:
        print("姓名:{0} 年龄:{1} 成绩:{2} ".format(i['name'], i['age'], i['score']))
