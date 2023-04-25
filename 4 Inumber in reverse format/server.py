import xmlrpc.server

# Define a function to reverse a number
def rev(num):
    rev_num = 0
    while num!=0:
        digit = num%10
        rev_num = rev_num *10 + digit
        num //= 10
    return rev_num

# Create an XML-RPC server instance
server = xmlrpc.server.SimpleXMLRPCServer(('localhost', 8000))

# Register the function with the server, and give it a name
server.register_function(rev, 'rev')

# Start the server and print a message
print('Server listening on port 8000...')
server.serve_forever()
