from collections import defaultdict, deque
import copy


def dfs(graph, root):
    """
    stack
    보통 재귀로 구현..
    """
    visited = [root]
    stack = sorted(graph[root], reverse=True)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
        stack += sorted(list(set(graph[node]) - set(visited)), reverse=True)
    return print(" ".join(list(map(str, visited))))


def bfs(graph, root):
    """queue"""
    visited = [root]
    queue = deque(graph[root])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
        queue += sorted(list(set(graph[node]) - set(visited)))
    return print(" ".join(list(map(str, visited))))


n, m, r = map(int, input().split())
dict_graph = defaultdict(list)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    dict_graph[start].append(end)
    dict_graph[end].append(start)
    dict_graph[start].sort()
    dict_graph[end].sort()

dfs(copy.deepcopy(dict_graph), r)
bfs(copy.deepcopy(dict_graph), r)
