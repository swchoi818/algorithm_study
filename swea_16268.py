T = int(input())

dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]

for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    balloon_list = []
    for _ in range(N):
        balloon_list.append(list(map(int,input().split())))
    max_cnt = 0
    for i in range(N):
        for j in range(M):
            cnt = balloon_list[i][j]
            for l in dir:
                x = i + l[0]
                y = j + l[1]
                if (0 <= x < N) and (0 <= y < M):
                    cnt += balloon_list[x][y]
            max_cnt = max(max_cnt, cnt)
    print(f"#{test_case}", max_cnt)