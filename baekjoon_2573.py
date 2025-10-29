import sys
from collections import deque

dir_4 = [(1, 0), (-1, 0), (0, -1), (0, 1)]

input = sys.stdin.readline


def melt_ice(mtr_copy):
    global mtr
    is_melted = False
    for i in range(N):
        for j in range(M):
            if mtr_copy[i][j] != 0:
                for dx, dy in dir_4:
                    nx = j + dx
                    ny = i + dy
                    if 0 <= nx < M and 0 <= ny < N and not mtr_copy[ny][nx] and mtr[i][j] > 0:
                        mtr[i][j] -= 1
                        if mtr[i][j] == 0:
                            is_melted = True
    return is_melted


def is_split():
    global mtr, time_cnt
    dq = deque()
    cnt = 0
    visited = list([False] * M for _ in range(N))
    for i in range(N):
        for j in range(M):
            if mtr[i][j] != 0 and not visited[i][j]:
                cnt += 1
                if cnt >= 2:
                    return True
                dq.append((i, j))
                visited[i][j] = True
                while dq:
                    y, x = dq.popleft()
                    for dx, dy in dir_4:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < M and 0 <= ny < N and mtr[ny][nx] and not visited[ny][nx]:
                            visited[ny][nx] = True
                            dq.append((ny, nx))
    if cnt == 0:
        time_cnt = 0
        return True
    return False


N, M = map(int, input().split())

mtr = [list(map(int, input().split())) for _ in range(N)]
time_cnt = 0

while True:
    if is_split():
        break
    time_cnt += 1
    melt_ice([i[:] for i in mtr])

print(time_cnt)
