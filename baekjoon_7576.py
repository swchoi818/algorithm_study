import sys

from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

mtr = [list(map(int, input().split())) for _ in range(N)]

dq = deque()

dir_4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
cnt_0 = 0
date = 0

for i in range(N):
    for j in range(M):
        if mtr[i][j] == 1:
            dq.append((i, j, date))
        elif mtr[i][j] == 0:
            cnt_0 += 1

while dq:
    y, x, date = dq.popleft()
    for dy, dx in dir_4:
        nx = x + dx
        ny = y + dy
        if 0 <= ny < N and 0 <= nx < M and mtr[ny][nx] == 0:
            dq.append((ny, nx, date + 1))
            mtr[ny][nx] = 1
            cnt_0 -= 1

if cnt_0 == 0:
    print(date)
else:
    print(-1)
