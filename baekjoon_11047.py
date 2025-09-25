N, K = map(int, input().split())

coin_value = [int(input()) for _ in range(N)]

result = 0

for i in range(N - 1, - 1, -1):
    if K == 0:
        break
    if K // coin_value[i] > 0:
        result += (K // coin_value[i])
        K = K % coin_value[i]

print(result)