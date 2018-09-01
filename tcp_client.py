from socket import *

# 创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)

# 发起连接请求
sockfd.connect(('127.0.0.1',8888))

while True:
    msg = input("Msg>>")
    if msg == "":
        break
    sockfd.send(msg.encode())
    data = sockfd.recv(1024)
    print(data.decode())

sockfd.close()