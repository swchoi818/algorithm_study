import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(node):
    global graph, result, visited, cnt
    while graph[node]:
        current_node = heapq.heappop(graph[node])
        if visited[current_node]:
            continue
        cnt += 1
        visited[current_node] = True
        result[current_node] = cnt
        dfs(current_node)

graph = defaultdict(list)

N, M, R = map(int, input().split())
result = [0] * (N + 1)
visited = [False] * (N + 1)
result[R] = 1
visited[R] = True
for i in range(M):
    u, v = map(int, input().split())
    heapq.heappush(graph[u], v)
    heapq.heappush(graph[v], u)
cnt = 1
dfs(R)

print(*result[1:], sep='\n')