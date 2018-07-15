from socket import *

host=input("Enter host: ")
port=int(input("Enter port: "))


def serverstart():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print("Listening for connections.. ")
    q, addr = s.accept()
    data = input("Enter Message :  ")
    q.send(data.encode())
    s.close()
