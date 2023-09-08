import socket

host = '0.0.0.0'
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

while True:
    client_socket, addr = server_socket.accept()

    data = client_socket.recv(1024).decode('utf-8')

    if data == 'open_usb':
        print("Opening USB ports...")
        # Perform the USB port opening operation here

    elif data == 'close_usb':
        print("Closing USB ports...")
        # Perform the USB port closing operation here

    else:
        print("Invalid command: ", data)

    response = "Command received: " + data
    client_socket.send(response.encode('utf-8'))

    client_socket.close()
