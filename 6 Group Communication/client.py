import socket

def start_client():
    # create a client socket using IPv4 and TCP protocol
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # define the server address as localhost on port 12345
    server_address = ('localhost', 12345)
    print(f'Connecting to {server_address[0]}:{server_address[1]}')
    
    # connect the client socket to the server socket
    client_socket.connect(server_address)
    
    # receive messages from the server until the connection is closed
    while True:
        message = client_socket.recv(1024)  # receive up to 1024 bytes of data
        if message:
            print(f'Received message: {message.decode("utf-8")}')  # decode the message and print it
        else:
            break
    
    # close the client socket
    client_socket.close()

if __name__ == '__main__':
    start_client()
