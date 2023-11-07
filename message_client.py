import socket
import threading

def send_messages(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode())

def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        print(message)

client_name = input("Enter your name: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
client_socket.connect(server_address)
client_socket.send(client_name.encode())

send_thread = threading.Thread(target=send_messages, args=(client_socket,))
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))

send_thread.start()
receive_thread.start()
