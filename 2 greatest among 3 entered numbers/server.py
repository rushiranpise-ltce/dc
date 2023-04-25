import xmlrpc.server

# function to find the greatest number
def find_greatest(num1, num2, num3):
    return max(num1, num2, num3)

# create a server object
server = xmlrpc.server.SimpleXMLRPCServer(('localhost', 8000))

# register the function with the server
server.register_function(find_greatest, 'find_greatest')

# start the server and listen for incoming requests
print('Server listening on port 8000...')
server.serve_forever()
