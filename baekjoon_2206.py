from collections import deque
import sys

input = sys.stdin.readline

dir_4 = [(0, 1), (-1, 0), (0, -1), (1, 0)]

N, M = map(int, input().split())

mtr = [list(input().strip()) for _ in range(N)]

dq = deque()
dq.append((0, 0, 1, 1))
visited = [[[False] * M for _ in range(N)] for _ in range(2)]
visited[1][0][0] = True
while dq:
    y, x, dist, wall = dq.popleft()
    if (y, x) == (N - 1, M - 1):
        print(dist)
        break
    for dy, dx in dir_4:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and not visited[wall][ny][nx]:
            visited[wall][ny][nx] = True
            if mtr[ny][nx] == '1' and wall:
                dq.append((ny, nx, dist + 1, wall - 1))
            elif mtr[ny][nx] == '0':
                dq.append((ny, nx, dist + 1, wall))

else:
    print(-1)