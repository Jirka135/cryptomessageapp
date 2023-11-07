import socket
import threading

# Dictionary to store connected clients and their sockets
clients = {}

# Function to handle a client connection
def handle_client(client_socket):
    client_name = client_socket.recv(1024).decode()
    clients[client_name] = client_socket

    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode()
            send_message_to_other_clients(client_name, message)
        except Exception as e:
            print(f"Error handling client {client_name}: {str(e)}")
            break

    del clients[client_name]
    print(f"Connection to {client_name} closed")
    client_socket.close()

# Function to send a message to other connected clients
def send_message_to_other_clients(sender_name, message):
    for name, socket in clients.items():
        if name != sender_name:
            try:
                socket.send(f"{sender_name}: {message}".encode())
            except Exception as e:
                print(f"Error sending message to {name}: {str(e)}")

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections (up to 5 clients in the queue)
server_socket.listen(5)
print("Server is listening for incoming connections...")

while True:
    client_socket, _ = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
