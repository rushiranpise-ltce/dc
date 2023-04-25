# import the xmlrpc.client module
import xmlrpc.client

# create a proxy object pointing to the XML-RPC server
proxy = xmlrpc.client.ServerProxy('http://localhost:8000/')

# prompt the user to enter three numbers
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

# call the remote method on the XML-RPC server to find the greatest number among the three input numbers
result = proxy.find_greatest(num1, num2, num3)

# display the result to the user
print(f"The greatest number is: {result}")
