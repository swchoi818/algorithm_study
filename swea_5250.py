import heapq

dir_4 = [(0, 1), (0, -1), (1, 0), (-1, 0)]

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    height_mtr = [list(map(int, input().split())) for _ in range(N)]
    distance = [[float('inf')] * N for _ in range(N)]
    distance[0][0] = 0
    hq = []
    heapq.heappush(hq, [0, (0, 0)])

    while hq:
        dist, loc = heapq.heappop(hq)
        y, x = loc
        if dist > distance[y][x]:
            continue

        for dy, dx in dir_4:
            ndist = dist + 1
            ny = y + dy
            nx = x + dx
            if 0 <= nx < N and 0 <= ny < N:
                if height_mtr[y][x] < height_mtr[ny][nx]:
                    ndist += (height_mtr[ny][nx] - height_mtr[y][x])
                if distance[ny][nx] > ndist:
                    distance[ny][nx] = ndist
                    heapq.heappush(hq, [ndist, (ny, nx)])

    print(f'#{t}', distance[N - 1][N - 1])

