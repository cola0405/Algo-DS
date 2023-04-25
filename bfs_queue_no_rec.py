# no recursion depends on queue
# double-ended queue
# 双端队列
from collections import deque

graph = {
    'A': {'B', 'C'},
    'B': {'D', 'E'},
    'C': {'F', 'G'},
    'D': {},
    'E': {'H'},
    'F': {'I'},
    'G': {'J'},
    'H': {},
    'I': {},
    'J': {}
}

def bfs(graph, start):
    queue = deque([start])
    visited = set()
    while queue:
        node = queue.popleft()
        print(node)

        # mark visited
        visited.add(node)

        # add new node
        for item in graph[node]:
            if item not in visited:
                queue.append(item)



start = 'A'
bfs(graph, start)





