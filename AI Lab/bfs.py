# Write a program using PROLOG/LISP to implement Depth First Search
from collections import deque

def bfs(graph, start, goal):
    queue = deque([[start]])  # Queue of paths
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = path + [neighbor]
                queue.append(new_path)

    return None

# Example graph as adjacency list
graph = {
    'a': ['b', 'c'],
    'b': ['d', 'e'],
    'c': ['f'],
    'd': [],
    'e': ['f'],
    'f': []
}

# Run BFS from 'a' to 'f'
result = bfs(graph, 'a', 'f')
print("BFS Path from 'a' to 'f':", result)
