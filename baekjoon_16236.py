import sys
from collections import deque
import heapq

DIR = [(-1, 0), (0, -1), (0, 1), (1, 0)]

input = sys.stdin.readline

N = int(input())
mtr = [list(map(int, input().split())) for _ in range(N)]

shark_size = 2
time = 0
result = 0
dq = deque()
visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if mtr[i][j] == 9:
            visited[i][j] = True
            mtr[i][j] = 0
            dq.append((i, j, 0, 0))
            break

nearest_fish = []

while dq:
    y, x, e, t = dq.popleft()
    if t == time and time > 0:
        e += 1
        y, x = heapq.heappop(nearest_fish)
        mtr[y][x] = 0
        if e == shark_size:
            shark_size += 1
            e = 0
        visited = [[False] * N for _ in range(N)]
        visited[y][x] = True
        dq.clear()
        nearest_fish.clear()
        dq.append((y, x, e, time))
        result = time
        time = 0
        continue
    for dy, dx in DIR:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < N and 0 <= nx < N and mtr[ny][nx] <= shark_size:
            if visited[ny][nx]:
                continue
            if mtr[ny][nx] == 0 or mtr[ny][nx] == shark_size:
                visited[ny][nx] = True
                dq.append((ny, nx, e, t + 1))
                continue
            heapq.heappush(nearest_fish, (ny, nx))
            time = t + 1
            visited[ny][nx] = True
            dq.append((ny, nx, e, t + 1))

print(result)