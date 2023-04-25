# List of available servers
servers = ['server1', 'server2', 'server3', 'server4', 'server5']

# Count of requests sent to each server
request_count = [0, 0, 0, 0, 0]

def get_least_loaded_server():
    # Returns the server with the minimum number of requests
    return servers[request_count.index(min(request_count))]

for i in range(10):
    least_loaded_server = get_least_loaded_server()
    print(f'Sending request {i+1} to {least_loaded_server}')
    # Increment the request count for the chosen server
    request_count[servers.index(least_loaded_server)] += 1
