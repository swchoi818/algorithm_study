T = int(input())

for t in range(1, T + 1):
    N, M, K = map(int, input().split())
    eta = sorted(list(map(int, input().split())))
    bun_cnt = 0
    cus_cnt = 0
    for i in eta:
        bun_cnt = i//M * K
        if bun_cnt - cus_cnt <= 0:
            print(f"#{t} Impossible")
            break
        cus_cnt += 1
    else:
        print(f"#{t} Possible")
