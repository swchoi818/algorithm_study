def dfs(start, cost, next_area):
    global battery_mtr, result
    if cost >= result:
        return
    if len(next_area) == 0:
        result = min(result, cost + battery_mtr[start][0])
        return
    for i in range(len(next_area)):
        dfs(next_area[i], cost + battery_mtr[start][next_area[i]], next_area[:i] + next_area[i + 1:])


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    battery_mtr = [list(map(int, input().split())) for _ in range(N)]
    result = float('inf')
    dfs(0, 0, list(range(1, N)))
    print(f'#{t}', result)
