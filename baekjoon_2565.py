N = int(input())

connect_list = []

for i in range(N):
    a, b = map(int, input().split())
    connect_list.append((a, b))
connect_list.sort()

result = 0
dp = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if connect_list[j][1] < connect_list[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)
    result = max(result, dp[i])

print(N - result)