edges = [
    (0, 1),
    (0, 2),
    (1, 2),
    (2, 0),
    (2, 3),
    (3, 3)
]

def build_undirected_graph(edges):
    graph = {}

    for a, b in edges:
        graph[a] = graph.get(a, [])
        graph[b] = graph.get(b, [])
    
        graph[a].append(b)
        graph[b].append(a)
    
def build_directed_graph(edges):
    graph = {}
    for a, b in edges:
        graph[a] = graph.get(a, [])
        graph[b] = graph.get(b, [])
    
        graph[a].append(b)
    
    return graph