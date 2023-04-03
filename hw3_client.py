import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 9000))
s.listen(2)
client, addr = s.accept()
print('Connection from ', addr)

while True:
    data = client.recv(1024)
    data = data.decode()
    if data == 'q':
        break

    data = eval(data)
    data = str(round(data, 1))
    client.send(data.encode())
    
client.close()
