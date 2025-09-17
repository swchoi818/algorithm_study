def dfs(idx, now_sum):
    global employee, result
    if result == 0:
        return
    if now_sum >= B:
        result = min(result, now_sum - B)
        return
    for i in range(idx, N):
        dfs(i + 1, now_sum + employee[i])


T = int(input())

for t in range(1, T + 1):
    N, B = map(int, input().split())
    employee = list(map(int, input().split()))
    result = float("inf")
    dfs(0, 0)

    print(f'#{t}', result)
