N, M = map(int, input().split())
num_list = [0] + list(map(int, input().split()))
remain_l = [0] * (N + 1)
remainder = {0: 1}

for i in range(1, N + 1):
    num_list[i] += num_list[i - 1]
    remain_l[i] = num_list[i] % M
    if remainder.get(remain_l[i]) is not None:
        remainder[remain_l[i]] += 1
    else:
        remainder[remain_l[i]] = 1
result = 0
for i in remainder.values():
    result += (i*(i-1) // 2)

print(result)
