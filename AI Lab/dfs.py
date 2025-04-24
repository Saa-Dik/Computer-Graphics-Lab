# Write a program using PROLOG/LISP to implement Depth First Search
def dfs(graph, start, goal, path=None, visited=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    path = path + [start]
    visited.add(start)

    if start == goal:
        return path

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, goal, path, visited)
            if new_path:
                return new_path

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

# Run DFS from 'a' to 'f'
result = dfs(graph, 'a', 'f')
print("DFS Path from 'a' to 'f':", result)
