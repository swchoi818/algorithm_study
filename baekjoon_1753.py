from heapq import heappush, heappop
from collections import defaultdict
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
distances = [float('inf')] * (V + 1)
distances[K] = 0

graph = defaultdict(list)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

hq = []
heappush(hq, (0, K))
while hq:
    dist, node = heappop(hq)
    if distances[node] < dist:
        continue
    for v, w in graph[node]:
        if distances[v] > dist + w:
            distances[v] = dist + w
            heappush(hq, (distances[v], v))

for i in range(1, V + 1):
    if distances[i] == float('inf'):
        print('INF')
        continue
    print(distances[i])

