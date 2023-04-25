import socket
def get_ip_address(url):
  try:
    host_name = socket.gethostbyname(url)
    host_ip = socket.gethostbyname(host_name)
    print("Hostname :",host_name)
    print("IP :",host_ip)
  except:
    print("Unable to get hostname and IP")
# Driver code
if _name_ == '_main_':
  url = "www.twitter.com"
  get_ip_address(url)