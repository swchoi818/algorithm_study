import heapq

T = int(input())

for t in range(1, T + 1):
    N, T = map(int, input().split())
    distance = [float('inf')] * N
    distance[0] = 0
    graph = {}
    hq = []
    for i in range(T):
        a, b, w = map(int, input().split())
        if graph.get(a):
            graph[a].append((b, w))
        else:
            graph[a] = [(b, w)]

    heapq.heappush(hq, [0, 0])

    while hq:
        dist, node = heapq.heappop(hq)
        if distance[node] < dist:
            continue
        if graph.get(node) == None:
            continue
        for n, w in graph[node]:
            ndist = dist + w
            if distance[n] > ndist:
                distance[n] = ndist
                heapq.heappush(hq, [ndist, n])
    if distance[N - 1] != float('inf'):
        print(f'#{t}', distance[N-1])
    else:
        print(f'#{t} impossible')