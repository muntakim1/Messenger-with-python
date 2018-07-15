import client
import server

print("Please Start Both server and Client pressing\n\t 1.Server \n\t 2.Client ")
print("Enter your option :")
x=int(input())

while True:
    if(x==1):
        server.serverstart()
    elif(x==2):
        client.Client()
    else:
        print("invalid")