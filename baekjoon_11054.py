N = int(input())
A = list(map(int, input().split()))
dpl = [1] * N
dpr = [0] * N
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dpl[i] = max(dpl[j] + 1, dpl[i])
for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, - 1):
        if A[i] > A[j]:
            dpr[i] = max(dpr[j] + 1, dpr[i])

    dpl[i] += dpr[i]

print(max(dpl))