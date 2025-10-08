import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

distance = [[float('inf')] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    distance[a][b] = min(distance[a][b], c)

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                distance[i][j] = 0
                continue
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if distance[i][j] == float('inf'):
            print(0, end=' ')
            continue
        print(distance[i][j], end=' ')
    print()
