from socket import * 

#处理请求,返回响应
def handleClient(connfd):
    print("Connect from",connfd.getpeername())
    request = connfd.recv(4096)
    # print(request)
    #按行进行分割
    requestHeadlers = request.splitlines()
    for line in requestHeadlers:
        print(line)

    #无论什么请求给出相同的响应
    try:
        f = open("index.html")
    except IOError:
        response = "HTTP/1.1  404  not found\r\n"
        response += '\r\n'
        response += "===Sorry,The page not found==="
    else:
        response = "HTTP/1.1  200  OK\r\n"
        response += '\r\n'
        for i in f:
            response += i 
    finally:
        connfd.send(response.encode())
    connfd.close() 

#网络链接控制流程
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(('0.0.0.0',8000))
    sockfd.listen(5)
    while True:
        print("Listen to the port 8000.....")
        connfd,addr = sockfd.accept()
        #处理具体客户端请求
        handleClient(connfd) 

if __name__ == "__main__":
    main()