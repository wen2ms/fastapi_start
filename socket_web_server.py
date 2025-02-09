import socket

sock = socket.socket()

sock.bind(('127.0.0.1', 8080))

sock.listen(5)

while True:
    connection, address = sock.accept()

    request_data = connection.recv(1024)

    print("Client request information\n", request_data)

    connection.send(b'HTTP/1.1 200 ok\r\nserver:local\r\n\r\nhello world')

    connection.close()
