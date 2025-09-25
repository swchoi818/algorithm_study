T = int(input())

for t in range(1, T + 1):
    N, E = map(int, input().split())
    distance = [float('inf')] * (N + 1)
    distance[0] = 0
    graph = {}
    result = 0

    for _ in range(E):
        a, b, w = map(int, input().split())
        if graph.get(a):
            graph[a][b] = w
        else:
            graph[a] = {b: w}

    for _ in range(N):
        is_updated = False
        for u in range(N):
            for v, w in graph[u].items():
                if distance[u] != float('inf') and distance[v] > distance[u] + w:
                    distance[v] = distance[u] + w
                    is_updated = True

        if not is_updated:
            break

    for u in range(N):
        for v, w in graph[u].items():
            if distance[u] != float('inf') and distance[v] > distance[u] + w:
                distance[N] = float('-inf')
                break
        if distance[N] == float('-inf'):
            break

    print(f'#{t}', distance[N])
