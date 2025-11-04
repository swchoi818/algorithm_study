import sys
import heapq
from collections import deque

DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def set_island(mtr):
    cnt = 0
    visited = [[False] * M for _ in range(N)]
    island = [[None]]
    for i in range(N):
        for j in range(M):
            if mtr[i][j] == 1 and not visited[i][j]:
                cnt += 1
                mtr[i][j] = cnt
                dq = deque()
                dq.append((i, j))
                visited[i][j] = True
                island.append([(i, j)])
                while dq:
                    y, x = dq.popleft()
                    for dy, dx in DIR:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and mtr[ny][nx] == 1:
                            mtr[ny][nx] = cnt
                            visited[ny][nx] = True
                            dq.append((ny, nx))
                            island[cnt].append((ny, nx))
    return island, cnt


def make_bridge(mtr, island, cnt):
    global hq
    visited = set()
    result = 0
    bridge_cnt = 0
    visited.add(1)
    find_bridge(mtr, island, 1)
    while hq:
        length, il_num = heapq.heappop(hq)
        if il_num not in visited:
            result += length
            bridge_cnt += 1
            visited.add(il_num)
            find_bridge(mtr, island, il_num)
            if bridge_cnt == cnt - 1:
                return result

    return -1

def find_bridge(mtr, island, il_num):
    global hq
    dq = deque()
    visited = set()
    for y, x in island[il_num]:
        for dy, dx in DIR:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and not mtr[ny][nx] and (ny, nx, dy, dx) not in visited:
                dq.append((ny, nx, dy, dx, 1))
                visited.add((ny, nx, dy, dx))
    while dq:
        y, x, dy, dx, length = dq.popleft()
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and (ny, nx, dy, dx) not in visited:
            if mtr[ny][nx] != il_num and mtr[ny][nx] != 0:
                if length > 1:
                    heapq.heappush(hq, (length, mtr[ny][nx]))
                continue
            visited.add((ny, nx, dy, dx))
            dq.append((ny, nx, dy, dx,  length + 1))

input = sys.stdin.readline

N, M = map(int, input().split())

hq = []

mtr = [list(map(int, input().split())) for _ in range(N)]

island, cnt = set_island(mtr)

print(make_bridge(mtr, island, cnt))