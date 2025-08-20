T = int(input())

for t in range(1, T + 1):
    N = int(input())
    carrot_list = list(map(int, input().split()))
    result = 0
    tmp_len = 1
    for i in range(1, N):
        if carrot_list[i] > carrot_list[i - 1]:
            tmp_len += 1
        else:
            result = max(result, tmp_len)
            tmp_len = 1
    result = max(result, tmp_len)
    print(f"#{t} {result}")