import sys

from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

maze_mtr = [list(input()) for _ in range(N)]

dq = deque()

dir_4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]

dq.append((0, 0, 1))
maze_mtr[0][0] = '0'
while dq:
    y, x, dist = dq.popleft()
    if (y, x) == (N - 1, M - 1):
        print(dist)
        break
    for dy, dx in dir_4:
        nx = x + dx
        ny = y + dy
        if 0 <= ny < N and 0 <= nx < M and maze_mtr[ny][nx] != '0':
            dq.append((ny, nx, dist + 1))
            maze_mtr[ny][nx] = '0'
