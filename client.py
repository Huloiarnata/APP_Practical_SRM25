import socket
import threading

# Define host and port
HOST = 'localhost'
PORT = 8000

# Create a socket object and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Define a function to receive messages from the server
def receive():
    while True:
        try:
            # Receive data from the server
            data = client_socket.recv(1024).decode()

            # Print the received message
            print(data)
        except:
            # Handle exceptions
            print("An error occurred!")
            client_socket.close()
            break

# Start a new thread to receive messages from the server
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# Send messages to the server
while True:
    message = input("")
    client_socket.send(message.encode())

    if message == "quit":
        client_socket.close()
        break
