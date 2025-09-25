T = int(input())

# 플로이드 워셜 - 시간 초과
# for t in range(1, T + 1):
#     N, M, X = map(int, input().split())
#     distance = [[float('inf')] * (N + 1) for _ in range(N + 1)]
#     for _ in range(M):
#         x, y, c = map(int, input().split())
#         distance[x][y] = c
#
#     for k in range(1, N + 1):
#         for i in range(1, N + 1):
#             for j in range(1, N + 1):
#                 if i == j:
#                     distance[i][j] = 0
#                     continue
#                 distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
#
#     result = 0
#     for i in range(1, N + 1):
#         if distance[i][X] != float('inf') and distance[X][i] != float('inf'):
#             result = max(result, distance[i][X] + distance[X][i])
#
#     print(f'#{t}', result)

# 다익스트라
import heapq

def dijkstra(graph, start, end, distance):
    hq = []
    heapq.heappush(hq, (0, start))

    while hq:
        dist, node = heapq.heappop(hq)
        if distance[node] < dist:
            continue
        for n, w in graph[node]:
            if distance[n] > dist + w:
                distance[n] = dist + w
                heapq.heappush(hq, (distance[n], n))

    return distance[end]

for t in range(1, T + 1):
    N, M, X = map(int, input().split())
    graph = {}
    for _ in range(M):
        x, y, c = map(int, input().split())
        if graph.get(x):
            graph[x].append((y, c))
        else:
            graph[x] = [(y, c)]

    to_x_dist = [float('inf')] * (N + 1)
    to_x_dist[X] = 0

    dijkstra(graph, X, N, to_x_dist)
    result = 0
    for i in range(1, N + 1):
        distance = [float('inf')] * (N + 1)
        distance[i] = 0
        result = max(result, dijkstra(graph, i, X, distance) + to_x_dist[i])

    print(f'#{t}', result)
