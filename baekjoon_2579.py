N = int(input())

stair_list = [int(input()) for _ in range(N)]
if len(stair_list) <= 2:
    print(sum(stair_list))
    exit(0)
dp = [0] * N
dp[0] = stair_list[0]
dp[1] = stair_list[0] + stair_list[1]
dp[2] = max(stair_list[0] + stair_list[2], stair_list[1] + stair_list[2])

for i in range(3, N):
    dp[i] = max(stair_list[i - 1] + dp[i - 3], dp[i - 2]) + stair_list[i]

print(dp[-1])
