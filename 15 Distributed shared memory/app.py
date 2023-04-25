import socket
import threading

SERVER_ADDRESS = 'localhost'
SERVER_PORT = 1234
nodes = {}

def handle_connection(conn, addr):
    # Receive node id from connection
    node_id = conn.recv(1024).decode()
    # Add node to nodes dictionary
    nodes[node_id] = conn
    
    while True:
        try:
            # Receive message from connection
            message = conn.recv(1024).decode()
            for node in nodes:
                # Send message to all other nodes except self
                if node != node_id:
                    nodes[node].sendall(message.encode())
        except:
            # Remove node from nodes dictionary if there is an error
            del nodes[node_id]
            break
    # Close connection when loop breaks
    conn.close()

# Create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind server socket to address and port
server_socket.bind((SERVER_ADDRESS, SERVER_PORT))
# Listen for incoming connections
server_socket.listen()
print(f"Central server listening on {SERVER_ADDRESS}:{SERVER_PORT}")

while True:
    # Accept incoming connection and pass it to handle_connection function in a new thread
    conn, addr = server_socket.accept()
    threading.Thread(target=handle_connection, args=(conn, addr)).start()