# Importing the xmlrpc server library
import xmlrpc.server

# Defining a function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Creating a SimpleXMLRPCServer object at "localhost" and port 8000
server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000))

# Registering the 'is_prime' function with the server and exposing it with the name 'is_prime'
server.register_function(is_prime, "is_prime")

# Starting the server and printing a message to indicate that it is listening on port 8000
print('Server listening on port 8000...')
server.serve_forever()
