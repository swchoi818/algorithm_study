for t in range(1, 11):
    n = int(input())
    str_list = [list(input()) for _ in range(8)]
    str_list2 = list(zip(*str_list))
    cnt = 0
    for i in range(8):
        for j in range(8 - n + 1):
            tmp1 = str_list[i][j:j + n]
            tmp2 = list(str_list2[i][j:j + n])
            if tmp1[:] == tmp1[::-1]:
                cnt += 1
            if tmp2[:] == tmp2[::-1]:
                cnt += 1
    print(f"#{t} {cnt}")