from collections import deque 

def path_pushing(source, sink, graph): 
    # Initialize residual graph 
    residual = {u: {v: graph[u][v] for v in graph[u]} for u in graph} 
    flow = 0 
    path = find_augmenting_path(source, sink, residual) 
    
    while path is not None: 
        # Calculate bottleneck capacity 
        bottleneck = min(residual[u][v] for u, v in path) 
        
        # Update residual capacities and flow 
        for u, v in path: 
            residual[u][v] -= bottleneck 
            residual[v][u] += bottleneck 
            
        flow += bottleneck 
        
        # Find next augmenting path 
        path = find_augmenting_path(source, sink, residual) 
        
    return flow 

def find_augmenting_path(source, sink, residual): 
    # Breadth-first search to find an augmenting path 
    visited = {v: False for v in residual} 
    visited[source] = True 
    queue = deque([(source, [])]) 
    
    while queue: 
        node, path = queue.popleft() 
        for neighbor in residual[node]: 
            if not visited[neighbor] and residual[node][neighbor] > 0: 
                visited[neighbor] = True 
                new_path = path + [(node, neighbor)] 
                
                if neighbor == sink: 
                    return new_path 
                
                queue.append((neighbor, new_path))
                
    return None
