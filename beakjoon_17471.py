import sys


# input = sys.stdin.readline().rstrip()

from collections import deque


def check_connection(area_l):
    global N, connect_dict
    visited = [False] * (N + 1)
    area_que = deque()
    area_que.append(area_l[0])
    visited[area_l[0]] = True
    cnt = 1
    while area_que:
        key = area_que.popleft()
        if connect_dict[key]:
            for i in connect_dict[key]:
                if visited[i] or i not in area_l:
                    continue
                visited[i] = True
                area_que.append(i)
                cnt += 1
    if cnt == len(area_l):
        return True


def dfs(select, remain, idx):
    global population_list
    if 0 < len(select) < N:
        if check_connection(select) and check_connection(remain):
            sum_a = sum(map(lambda x: population_list[x - 1], select))
            sum_b = sum(map(lambda x: population_list[x - 1], remain))
            result.append(abs(sum_a - sum_b))
    for i in range(idx, len(remain)):
        select.append(remain[i])
        dfs(select, remain[:i] + remain[i + 1:], i)
        select.pop()


N = int(input())

population_list = list(map(int, input().split()))

connect_dict = {}
result = []
is_connect = False

if N == 2:
    result.append(abs(population_list[0] - population_list[1]))
else:
    for i in range(1, N + 1):
        values = list(map(int, input().split()))
        if values[0] == 0:
            connect_dict[i] = None
            continue
        is_connect = True
        connect_dict[i] = values[1:]
    if is_connect:
        dfs([], list(range(1, N + 1)), 0)
if not result:
    result.append(-1)
print(min(result))
