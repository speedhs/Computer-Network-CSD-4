import socket



client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('localhost', 12345))



packetCount=10

spaces = 5

while True :

    if spaces>0 :

        client_socket.sendall(b'hello')

        print("sent")

        spaces-=1

        packetCount-=1

        if packetCount==0 :

            break

    else :

        ack = client_socket.recv(1024)

        if ack == b'ACK':

            print('ACK received')

        spaces+=1



client_socket.close()