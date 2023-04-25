# This program demonstrates how to use an XML-RPC client to call a function on an XML-RPC server

import xmlrpc.client


# create an instance of the server proxy by passing the URL of the server
proxy = xmlrpc.client.ServerProxy('http://localhost:8000/')

# ask user to enter a value for n
n = int(input("enter value of n: "))

# call the "fib" function on the server and store the result in "result"
result = proxy.fib(n)

# display the result
print(f"The fibonacci series upto n is: {result}")
