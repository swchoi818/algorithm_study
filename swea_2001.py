T = int(input())
 
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    num_mtr = []
    for _ in range(N):
        num_mtr.append(list(map(int,input().split())))
    max_cnt = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            cnt = 0
            for k in range(M):
                for l in range(M):
                    cnt += num_mtr[i+k][j+l]
            max_cnt = max(cnt, max_cnt)
            
    print(f"#{test_case}", max_cnt)