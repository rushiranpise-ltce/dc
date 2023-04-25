import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    print(f'Starting server on {server_address[0]}:{server_address[1]}')
    
    # Bind the socket to a specific address and port
    server_socket.bind(server_address)
    
    # Listen for incoming connections, with a backlog of 5
    server_socket.listen(5)
    
    # Create a list to keep track of all connected clients
    clients = []
    
    while True:
        print('Waiting for connections...')
        # Accept a new connection
        client_socket, client_address = server_socket.accept()
        print(f'Accepted connection from {client_address[0]}:{client_address[1]}')
        
        # Send a welcome message to the new client
        client_socket.send(b'Welcome to the group!')
        
        # Add the new client to the list of connected clients
        clients.append(client_socket)
        
        # Send a message to all connected clients (except the new one) that a new member joined
        for client in clients:
            if client != client_socket:
                client.send(b'A new member joined the group!')
                
    server_socket.close()

if __name__ == '__main__':
    start_server()
