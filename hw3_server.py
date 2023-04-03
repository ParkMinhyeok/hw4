import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

while(True):
    text = input("input : ")
    if(text == 'q'):
        break

    sock.send(text.encode())
    text = sock.recv(1024)
    print(text.decode())

sock.close()
