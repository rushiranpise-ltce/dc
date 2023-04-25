import xmlrpc.server

def fib(n):
    num = n
    list = []
    n1, n2 = 0, 1
    list.append(n1)
    list.append(n2)
    print("Fibonacci Series:", n1, n2, end=" ")
    for i in range(2, num):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        list.append(n3)
    return list

# create a server instance
server = xmlrpc.server.SimpleXMLRPCServer(('localhost', 8000))

# register the function fib() with the server and give it a name 'fib'
server.register_function(fib, 'fib')

print('Server listening on port 8000...')

# start the server and wait for incoming requests
server.serve_forever()
