T = int(input())
for _ in range(T):
    N = int(input())
    tmp1 = 1
    tmp2 = 1
    tmp3 = 1
    result = 1
    for i in range(3, N):
        result = tmp1 + tmp2
        tmp1, tmp2 = tmp2, tmp3
        tmp3 = result

    print(result)
