N = int(input())

wine_list = [int(input()) for _ in range(N)]
dp = [0] * N
if N < 3:
    print(sum(wine_list))
else:
    dp[0] = wine_list[0]
    dp[1] = wine_list[0] + wine_list[1]
    dp[2] = max(wine_list[1] + wine_list[2], dp[1], dp[0] + wine_list[2])

    for i in range(3, N):
        dp[i] = max(dp[i - 3] + wine_list[i - 1] + wine_list[i], dp[i - 2] + wine_list[i], dp[i - 1])

    print(dp[N - 1])