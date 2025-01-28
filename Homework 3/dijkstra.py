from heapq import heappop, heappush

def dijkstra(graph, source, target):
    # Initialization
    dist = { vertex: float('inf') for vertex in graph }
    prev = { vertex: None for vertex in graph }
    dist[source] = 0
    
    # Priority queue storing (distance, node)
    heap = [(0, source)]
    
    while heap:
        current_dist, u = heappop(heap)
        
        # Skip if a shorter path to u has been found
        if current_dist > dist[u]: continue
        
        for v, weight in graph[u]:
            alt = dist[u] + weight
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heappush(heap, (alt, v))

    path = [ ]
    current = target
    
    while current:
        path.insert(0, current)
        current = prev[current]

    return path

if __name__ == "__main__":
    # Define the graph as an adjacency list
    graph = {
        'start': [('1', 7)],
        '1': [('2', 6)],
        '2': [('3', 5)],
        '3': [('4', 4)],
        '4': [('5', 3), ('6', 3)],
        '5': [('7', 6)],
        '6': [('8', 2)],
        '7': [('9', 5)],
        '8': [('10', 3), ('11', 1)],
        '9': [('12', 4)],
        '10': [('13', 2)],
        '11': [('goal', 0)],
        '12': [('14', 3)],
        '13': [],
        '14': [('15', 2)],
        '15': [],
        'goal': []
    }
    
    source, target = 'start', 'goal'

    path = dijkstra(graph, source, target)

    print(f"Shortest path from {source} to {target}: {' -> '.join(path)}")