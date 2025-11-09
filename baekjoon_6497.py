import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

while True:
    M, N = map(int, input().split())
    if N == 0 and M == 0:
        break
    graph = defaultdict(list)
    result = 0
    for _ in range(N):
        x, y, w = map(int, input().split())
        graph[x].append((y, w))
        graph[y].append((x, w))
        result += w

    hq = []
    visited = set()
    heapq.heappush(hq, (0, 0))

    while hq:
        weight, node = heapq.heappop(hq)
        if node in visited:
            continue
        visited.add(node)
        result -= weight
        if len(visited) == N:
            break

        for n, w in graph[node]:
            if n in visited:
                continue
            heapq.heappush(hq, (w, n))

    print(result)