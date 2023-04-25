# Importing required modules
import socket

# Defining function to get IP address of a URL
def get_ip_address(url):
    try:
        # Getting the IP address of the given URL
        host_name = socket.gethostbyname(url)
        host_ip = socket.gethostbyname(host_name)
        # Printing the host name and IP address
        print("Hostname :", host_name)
        print("IP :", host_ip)
    except:
        # Handling the exception if IP address is not found
        print("Unable to get hostname and IP")
# Driver code
if __name__ == "__main__":
    # Testing the function with a sample URL
    url = "www.twitter.com"
    get_ip_address(url)
