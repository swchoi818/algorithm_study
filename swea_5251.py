def dfs(sum_cal, sum_taste, idx):
    global hamburger_list, result
    if sum_cal > L:
        return
    if result < sum_taste:
        result = sum_taste
    for i in range(idx, len(hamburger_list)):
        dfs(sum_cal + hamburger_list[i][1], sum_taste + hamburger_list[i][0], i + 1)


T = int(input())

for t in range(1, T + 1):
    N, L = map(int, input().split())
    hamburger_list = [tuple(map(int, input().split())) for _ in range(N)]
    result = 0
    dfs(0, 0, 0)
    print(f"#{t}", result)
