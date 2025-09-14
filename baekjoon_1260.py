from collections import deque

N, M, V = map(int, input().split())

graph_dict = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    key, value = map(int, input().split())
    graph_dict[key].append(value)
    graph_dict[value].append(key)
result = [[] for _ in range(2)]
visited = [False] * (N + 1)
dfs_stack = [V]
visited[V] = True
result[0].append(V)
while dfs_stack:
    root = dfs_stack[-1]

    next_node = None
    for node in sorted(graph_dict[root]):
        if not visited[node]:
            next_node = node
            break

    if next_node:
        visited[next_node] = True
        result[0].append(next_node)
        dfs_stack.append(next_node)
    else:
        dfs_stack.pop()

visited = [False] * (N + 1)
bfs_queue = deque()
bfs_queue.append(V)
visited[V] = True
result[1].append(V)
while bfs_queue:
    root = bfs_queue.popleft()
    for node in sorted(graph_dict[root]):
        if visited[node]:
            continue
        visited[node] = True
        bfs_queue.append(node)
        result[1].append(node)

print(*result[0])
print(*result[1])
