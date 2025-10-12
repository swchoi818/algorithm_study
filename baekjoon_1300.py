N = int(input())
K = int(input())

st = 0
end = K
result = 0

while st <= end:
    mid = (st + end) // 2
    count = 0
    for i in range(1, N + 1):
        count += min(N, mid // i)

    if count >= K:
        result = mid
        end = mid - 1
    else:
        st = mid + 1

print(result)