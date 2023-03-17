import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 23567))
server_socket.listen(1)

connection, client_address = server_socket.accept()

data = connection.recv(1024)

if data == b'hello':
    print('hello received')
    connection.sendall(b'ACK')

connection.close()
server_socket.close()
