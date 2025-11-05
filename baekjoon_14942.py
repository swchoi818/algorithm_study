import sys
from collections import defaultdict
input = sys.stdin.readline


def dfs(node, dist):
    global result, graph, energy, visited, distances
    if dist - energy[node - 1] <= 0:
        result[node] = 1
    else:
        result[node] = binary_search(dist - energy[node - 1])

    for i, w in graph[node]:
        if visited[i]:
            continue
        visited[i] = True
        distances.append((i, dist + w))
        dfs(i, dist + w)
        distances.pop()


def binary_search(target):
    global distances
    start = 0
    end = len(distances)
    while end > start:
        middle = (start + end) // 2
        n, dist = distances[middle]
        if dist < target:
            start = middle + 1
        else:
            end = middle
    return distances[start][0]


N = int(input())

energy = [int(input()) for _ in range(N)]

graph = defaultdict(list)
for _ in range(N-1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

distances = [(1, 0)]
visited = [False] * (N + 1)
result = [0] * (N + 1)

visited[1] = True
dfs(1, 0)

print(*result[1:], sep='\n')
