# Importing the xmlrpc client library
import xmlrpc.client

# Creating a proxy object for the server at "http://localhost:8000"
proxy = xmlrpc.client.ServerProxy("http://localhost:8000")

# Taking input from the user and converting it to an integer
n = int(input("Enter a number: "))

# Calling the 'is_prime' method on the server with the user input as argument and storing the result
result = proxy.is_prime(n)

# Printing the result returned from the server
print(result)
