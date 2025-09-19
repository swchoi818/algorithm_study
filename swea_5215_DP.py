T = int(input())

for t in range(1, T + 1):
    N, L = map(int, input().split())
    hamburger_list = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(N)]
    dp = [[0] * (L + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        cur_s, cur_c = hamburger_list[i]
        for j in range(1, L + 1):
            if cur_c >= j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cur_c] + cur_s)

    print(f'#{t}', dp[N][L])
