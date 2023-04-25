# Define a list of servers and initialize their request count to 0
servers = ['server1', 'server2', 'server3', 'server4']
request_count = [0, 0, 0, 0]

# Define a function to get the least loaded server
def get_least_loaded_server():
    # Find the server with the least number of requests 
    return servers[request_count.index(min(request_count))]

# Simulate sending 10 requests
for i in range(10):
    # Get the least loaded server
    least_loaded_server = get_least_loaded_server()

    # Send the request to the least loaded server
    print(f'Sending request {i+1} to {least_loaded_server}')

    # Increment the request count for the least loaded server
    request_count[servers.index(least_loaded_server)] += 1
