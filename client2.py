import socket
import threading

HOST = 'localhost'  # the server's hostname or IP address
PORT = 8000        # the port used by the server

# function to handle incoming messages from the server
def handle_messages(sock):
    while True:
        # receive data from the server
        data = sock.recv(1024)
        if not data:
            break
        # print the message to the console
        print(data.decode())

# create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # connect to the server
    s.connect((HOST, PORT))
    # create a new thread to handle incoming messages from the server
    thread = threading.Thread(target=handle_messages, args=(s,))
    thread.start()
    # send messages to the server
    while True:
        message = input()
        # send the message to the server
        s.sendall(message.encode())
