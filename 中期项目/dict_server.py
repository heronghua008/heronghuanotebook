
'''
name:Levi
date:2018-10-10
email:lvze@tedu.cn
modules: python3.5  pymysql
This is a dict project for AID class
'''
from socket import * 
import os 
import signal 
import time 
import pymysql 
import sys 

DICT_TEXT = './dict.txt'
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST,PORT)

#主控制流程
def main():
    #数据库链接
    db = pymysql.connect\
    ('localhost','mark','123456','dict')

    #创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)

    #忽略子进程退出
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    while True:
        try:
            c,addr = s.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue

        #创建子进程
        pid = os.fork()
        if pid < 0:
            print("create process failed")
            c.close()
        elif pid == 0:
            s.close()
            do_child(c,db) 
        else:
            c.close()

def do_child(c,db):
    #循环接受请求
    while True:
        data = c.recv(128).decode()
        print("Request:",data)
        if (not data) or data[0] == 'E':
            c.close()
            sys.exit(0)
        elif data[0] == 'R':
            do_register(c,db,data)
        elif data[0] == 'L':
            do_login(c,db,data)
        elif data[0] == 'Q':
            do_query(c,db,data) 
        elif data[0] == 'H':
            do_history(c,db,data)

def do_register(c,db,data):
    print("注册操作")
    l = data.split(' ')
    name = l[1]
    passwd = l[2]
    cursor = db.cursor()

    sql = "select * from user where name='%s'"%name
    cursor.execute(sql)
    r = cursor.fetchone()
    if r != None:
        c.send(b'EXISTS')
        return

    sql = "insert into user (name,passwd) values\
     ('%s','%s')"%(name,passwd)

    try:
        cursor.execute(sql)
        db.commit()
        c.send(b'OK')
    except:
        c.send(b'FALL')
        db.rollback()
        return 
    else:
        print("%s注册成功"%name)


def do_login(c,db,data):
    print("登录操作")
    l = data.split(' ')
    name = l[1]
    passwd = l[2]
    cursor = db.cursor()

    sql = "select * from user \
    where name='%s' and passwd='%s'"%(name,passwd)

    cursor.execute(sql)
    r = cursor.fetchone()

    if r == None:
        c.send(b'FALL')
    else:
        c.send(b'OK')


def do_query(c,db,data):
    print("查询操作") 
    l = data.split(' ')
    name = l[1]
    word = l[2]
    cursor = db.cursor()

    def insert_history():
        tm = time.ctime()
        sql = "insert into hist (name,word,time)\
         values ('%s','%s','%s')"%(name,word,tm)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
            return

    #文本查找
    try:
        f = open(DICT_TEXT,'rb')
    except:
        c.send(b'FALL')
        return
    while True:
        line = f.readline().decode()
        tmp = line.split(' ')
        if tmp[0] > word:
            c.send(b'FALL')
            break
        if tmp[0] == word:
            c.send(b'OK')
            time.sleep(0.1)
            c.send(line.encode())
            insert_history()
            break 
        if not line:
            c.send(b'FALL')
            break
    f.close()

def do_history(c,db,data):
    print("历史记录")
    name = data.split(' ')[1]
    cursor = db.cursor()
    try:
        sql = "select * from hist where name='%s'"%name
        cursor.execute(sql)
        r = cursor.fetchall()
        if not r:
            c.send(b'FALL')
            return
        else:
            c.send(b'OK')
    except:
        c.send(b'FALL')
        return  
    for i in r:
        time.sleep(0.1)
        msg = '%s   %s   %s'%(i[1],i[2],i[3])
        c.send(msg.encode())
    time.sleep(0.1)
    c.send(b'##')


if __name__ == "__main__":
    main()

