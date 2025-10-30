import sys
import heapq
from collections import deque, defaultdict

input = sys.stdin.readline


def dijkstra(graph, x):
    hq = []
    distances = [float('inf')] * (N + 1)
    heapq.heappush(hq, (0, x))
    while hq:
        dist, node = heapq.heappop(hq)
        if distances[node] < dist:
            continue

        distances[node] = dist

        for w, v in graph[node]:
            if distances[v] > dist + w:
                distances[v] = dist + w
                heapq.heappush(hq, (w + dist, v))

    return distances[:]


N, M, X = map(int, input().split())

graph = defaultdict(list)
reverse_graph = defaultdict(list)

for _ in range(M):
    v1, v2, w = map(int, input().split())
    graph[v1].append((w, v2))
    reverse_graph[v2].append((w, v1))

dists = dijkstra(graph, X)
dists2 = dijkstra(reverse_graph, X)
result = []

for i in range(1, N + 1):
    result.append(dists[i] + dists2[i])

print(max(result))
