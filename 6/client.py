import socket

def start_client():
    # create a client socket using IPv4 and TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # specify the address of the server to connect to
    server_address = ('localhost', 12345)
    
    # print a message indicating that the client is connecting to the server
    print(f'Connecting to {server_address[0]}:{server_address[1]}')
    
    # connect the client socket to the server at the specified address
    client_socket.connect(server_address)

    # receive messages from the server in a loop until no more messages are received
    while True:
        message = client_socket.recv(1024) # receive up to 1024 bytes of data
        if message:
            # print the received message after decoding it from bytes to string using utf-8 encoding
            print(f'Received message: {message.decode("utf-8")}')
        else:
            # break out of the loop if no more messages are received
            break

    # close the client socket when done receiving messages
    client_socket.close()

if __name__ == '__main__':
    # start the client program
    start_client()
