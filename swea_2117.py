from collections import deque

dir_4 = [(0, 1), (0, -1), (1, 0), (-1, 0)]

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    city_mtr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            visited = [[False] * N for _ in range(N)]
            bfs_deq = deque()
            bfs_deq.append((i, j, 1))
            visited[i][j] = True
            cost = 1
            house_cnt = [0] * (2 * N)

            if city_mtr[i][j] == 1:
                house_cnt[1] = 1

            while bfs_deq:
                y, x, dist = bfs_deq.popleft()

                if dist >= N * 2:
                    continue

                for dy, dx in dir_4:
                    ny, nx = y + dy, x + dx

                    if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx]:
                        visited[ny][nx] = True
                        bfs_deq.append((ny, nx, dist + 1))

                        if city_mtr[ny][nx] == 1:
                            house_cnt[dist + 1] += 1
            tmp_sum = 0
            for k in range(1, 2 * N):
                cost = k ** 2 + (k - 1) ** 2
                tmp_sum += house_cnt[k]
                if 0 <= ((tmp_sum * M) - cost):
                    result = max(result, tmp_sum)

    print(f"#{t}", result)
