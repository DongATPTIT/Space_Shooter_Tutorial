import socket
from hashlib import *
key = 'B20DCAT206'
Server_name = '127.0.0.1'
Server_port = 8888
Server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#socket.AF_INET (tham so truyen vao phien ban IP chung ta se su dung o day la phien ban 4)
#socket.SOCK_STREAM chi loai ket noi TCP IP hoac UDP,... (o day dung TCP)

#gan dia chi ip cho socket bind(host, port) voi cac tham so la may chu va cong
Server_socket.bind(('127.0.0.1',Server_port))
#chi chap nhan 1 ket noi
Server_socket.listen(1)

c, addr = Server_socket.accept()
#Cho/chap nhan ket noi accept (). Ham nay tra ve 2 gia tri c: ket noi và addr: dia chi cua request hoac dia chi client
ClientMessage = c.recv(1024).decode() #thong diep cua client
HashClient = c.recv(1024).decode() #thong diep bam cua client
#recv: doc du lieu duoc server gui toi voi 1024 bytes
#decode: phan tich du lieu duoc nhan
print('From:',addr,ClientMessage)
if HashClient != sha512(ClientMessage.encode("utf-8")+key.encode("utf-8")).hexdigest():
    print("The received message has lost its integrity.")
    ServerMessage = "The received message has lost its integrity."
    c.send(ServerMessage.encode())
else:
    ServerMessage = "Xin chao day la B20DCAT206-Dong Server" #thong diep cua server
    c.send(ServerMessage.encode()) #gui thong diep cua server
    #encode: ma hoa du lieu
c.close()
