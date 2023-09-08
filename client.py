import socket

server_ip = 'server_ip_address'
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

while True:
    command = input("Enter 'open' to open USB ports, 'close' to close: ")

    if command == 'open' or command == 'close':
        client_socket.send(command.encode('utf-8'))

        response = client_socket.recv(1024).decode('utf-8')
        print("Server response:", response)

    else:
        print("Invalid command. Enter 'open' or 'close'.")

client_socket.close()
