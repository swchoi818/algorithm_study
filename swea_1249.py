from collections import deque

dir_4 = [(-1, 0), (1, 0), (0, 1), (0, -1)]

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    map_mtr = [list(map(int, input())) for _ in range(N)]
    memo_mtr = [[-1] * N for _ in range(N)]
    memo_mtr[0][0] = 0
    dq = deque()
    dq.append((0, 0))
    while dq:
        y, x = dq.popleft()
        if (y, x) == (N - 1, N - 1):
            continue
        for dy, dx in dir_4:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < N:
                if memo_mtr[ny][nx] != -1 and memo_mtr[y][x] + map_mtr[ny][nx] >= memo_mtr[ny][nx]:
                    continue
                memo_mtr[ny][nx] = memo_mtr[y][x] + map_mtr[ny][nx]
                dq.append((ny, nx))

    print(f'#{t}', memo_mtr[N - 1][N - 1])
