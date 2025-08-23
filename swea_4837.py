def dfs(num, depth, idx):
    global cnt
    if depth == N and num == K:
        cnt += 1
        return
    if num >= K:
        return
    for i in range(idx + 1, 13):
        dfs(num + i, depth + 1, i)


T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    cnt = 0
    dfs(0, 0, 0)

    print(f"#{t}", cnt)
