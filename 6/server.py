import socket

# Define a function to start the server
def start_server():
    # Create a new socket using IPv4 address family and TCP protocol
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Specify the server address and port number
    server_address = ('localhost', 12345)

    # Print a message indicating that the server is starting
    print(f'Starting server on {server_address[0]}:{server_address[1]}')

    # Bind the socket to the server address and port number
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(5)

    # Create an empty list to store client sockets
    clients = []

    # Loop indefinitely to wait for and handle client connections
    while True:
        # Print a message indicating that the server is waiting for connections
        print('Waiting for connections...')

        # Accept a new connection from a client
        client_socket, client_address = server_socket.accept()

        # Print a message indicating that a new connection has been accepted
        print(f'Accepted connection from {client_address[0]}:{client_address[1]}')

        # Send a welcome message to the client
        client_socket.send(b'Welcome to the group!')

        # Add the client socket to the list of clients
        clients.append(client_socket)

        # Loop through all connected clients and send a notification message to each one except the current client
        for client in clients:
            if client != client_socket:
                client.send(b'A new member joined the group!')

    # Close the server socket when the loop ends
    server_socket.close()

if __name__ == '__main__':
    # Call the start_server function when the script is run as the main program
    start_server()
