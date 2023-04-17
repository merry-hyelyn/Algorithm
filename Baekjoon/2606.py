from collections import defaultdict, deque
'''
bfs
'''


def dfs(graph, root=1):
    visited = [root]
    stack = graph[root]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    print(visited)
    return len(visited) - 1


def bfs(graph, root):
    pass


n = int(input())
m = int(input())

graph = defaultdict(list)

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
print(graph)
print(dfs(graph, 1))
