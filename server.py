import socket
#khoi tao socket server
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#dat cong cua socket
server_port = 8888
#lien ket dia chi IP va cong voi socket server
server_socket.bind(('localhost',server_port))
#cho ket noi tu client
server_socket.listen(1)
print('Server dang cho ket noi')
#xu ly ket noi tu client
while True:
    #chap nhan ket noi tu client
    client_socket,client_address = server_socket.accept()
    print(f'da ket noi toi {client_address}')  
    #nhan du lieu tu client
    data = client_socket.recv(1024)
    print(f'From Client: {data.decode()}') 
    #gui du lieu tra ve cho client
    message = 'Xin chao, day la B20DCAT206-Dong Server'
    client_socket.sendall(message.encode())
    #dong ket noi voi client
    client_socket.close()