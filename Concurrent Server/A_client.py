import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 23567))
x=input()
if(x=='hello'):
    client_socket.sendall(b'hello')

    ack = client_socket.recv(1024)

    if ack == b'ACK':
        print('ACK received')

client_socket.close()


