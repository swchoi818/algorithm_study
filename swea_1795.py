T = int(input())

for t in range(1, T + 1):
    N, M, X = map(int, input().split())
    distance = [[float('inf')] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        distance[x][y] = c

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if i == j:
                    distance[i][j] = 0
                    continue
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    result = 0
    for i in range(1, N + 1):
        if distance[i][X] != float('inf') and distance[X][i] != float('inf'):
            result = max(result, distance[i][X] + distance[X][i])

    print(f'#{t}', result)
