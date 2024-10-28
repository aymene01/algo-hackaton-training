adj_list = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

from collections import deque


def dfs(graph, src, visited):
    if src in visited:
        return

    print(src)
    visited.add(src)

    for neighbor in graph[src]:
        dfs(graph, neighbor, visited)

def bfs(graph, src):
    visited = set([ src ])
    queue = deque([ src ])

    while queue:
        current = queue.popleft()
        print(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


    
print("DFS:")
dfs(adj_list, 0, set())

print("\nBFS:")
bfs(adj_list, 0)