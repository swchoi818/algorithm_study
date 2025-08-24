N, K = map(int, input().split())
num_list = [0] + list(map(int, input().split()))
for i in range(1, N + 1):
    num_list[i] += num_list[i - 1]
result = []
for i in range(K, N + 1):
    result.append(num_list[i] - num_list[i - K])

print(max(result))
