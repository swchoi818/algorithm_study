N = int(input())

tmp = 1
result = 2
if N == 1:
    print(tmp)
    exit(0)
for _ in range(N - 2):
    result, tmp = (tmp + result)%15746, result

print(result)
