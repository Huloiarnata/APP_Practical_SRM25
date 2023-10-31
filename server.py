import socket
import threading

# Define host and port
HOST = 'localhost'
PORT = 8000

# Create a socket object and bind it to the host and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

# Define a function to handle client connections
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        # Receive data from the client
        data = conn.recv(1024).decode()

        if data == "quit":
            connected = False
        else:
            # Print the received message
            print(f"[{addr}] {data}")

            # Send the message to all clients except the sender
            for client in clients:
                if client != conn:
                    client.send(data.encode())

    # Close the connection
    conn.close()
    print(f"[DISCONNECTED] {addr} disconnected.")

# Define a list to store all connected clients
clients = []

# Start listening for client connections
server_socket.listen()

print(f"[LISTENING] Server is listening on {HOST}:{PORT}")

while True:
    # Accept a client connection
    conn, addr = server_socket.accept()

    # Add the client connection to the list
    clients.append(conn)

    # Start a new thread to handle the client connection
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
