import xmlrpc.client

# create a proxy object to access the remote XML-RPC server
proxy = xmlrpc.client.ServerProxy('http://localhost:8000/')

# get input from the user
n = int(input("enter number: "))

# call the remote method 'rev' with the input number as parameter
result = proxy.rev(n)

# display the result
print(f"The reversed number is: {result}")
