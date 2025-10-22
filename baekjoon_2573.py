import sys
from collections import deque

dir_4 = [(1, 0), (-1, 0), (0, -1), (0, 1)]

input = sys.stdin.readline

N, M = map(int, input().split())

mtr = [list(map(int, input().split())) for _ in range(N)]
melt_value = list([0] * M for _ in range(N))

for i in range(N):
    for j in range(M):
        if j != 0:
            for dx, dy in dir_4:
                nx = j + dx
                ny = i + dy
                if 0 <= nx < M and 0 <= ny < N and not mtr[ny][nx]:
                    melt_value[i][j] += 1
time_cnt = 0
is_all_melted = False
while True:
    is_melted = False
    is_all_melted = True
    next_melt = [[i] for i in melt_value]
    for i in range(N):
        for j in range(M):
            if mtr[i][j] != 0:
                is_all_melted = False
                mtr[i][j] -= melt_value[i][j]
                if mtr[i][j] <= 0:
                    mtr[i][j] = 0
                    is_melted = True
                    next_melt[i][j] = 0
                    for dx, dy in dir_4:
                        nx = j + dx
                        ny = i + dy
                        if 0 <= nx < M and 0 <= ny < N and next_melt[ny][nx]:
                            next_melt[ny][nx] += 1
    melt_value = [[i] for i in next_melt]
    time_cnt += 1
    if is_melted:
        dq = deque()
        cnt = 0
        visited = list([False] * M for _ in range(N))
        for i in range(N):
            for j in range(M):
                if mtr[i][j] != 0 and not visited[i][j]:
                    cnt += 1
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
    if cnt >= 2:
        break
    if is_all_melted:
        time_cnt = 0
        break
print(time_cnt)
