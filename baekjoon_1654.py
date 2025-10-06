K, N = map(int, input().split())

lan_len = [int(input()) for _ in range(K)]

high = max(lan_len)
low = 1
result = 0
while low <= high:
    mid = (low + high) // 2
    l_sum = 0
    for l in lan_len:
        if l//mid > 0:
            l_sum += (l//mid)
    if l_sum >= N:
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)

