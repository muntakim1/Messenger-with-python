from socket import *
import server
host=server.host
port=server.port

def Client():
    s = socket(AF_INET, SOCK_STREAM)
    print("Connected")
    s.connect((host, port))
    msg = s.recv(1024)
    print("Message from server: " + msg.strip().decode('ascii'))
    s.close()