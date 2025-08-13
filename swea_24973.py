T = int(input())

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for t in range(1, T + 1):
    N = int(input())
    map_mtr = [list(map(int, input().split())) for _ in range(N)]
    st_xy = []
    res_cnt = []
    max_height = 0
    for i in range(N):
        for j in range(N):
            if max_height <= map_mtr[i][j]:
                if st_xy and max_height != map_mtr[i][j]:
                    st_xy.pop()
                max_height = map_mtr[i][j]
                st_xy.append((j, i))

    for sx, sy in st_xy:
        cnt = 0
        is_end = False
        while not is_end:
            is_end = True
            x = sx
            y = sy
            cnt += 1
            min_height = map_mtr[y][x]
            for dx, dy in dxy:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < N and 0 <= ny < N and min_height > map_mtr[ny][nx]:
                    min_height = map_mtr[ny][nx]
                    sx = nx
                    sy = ny
                    is_end = False
        res_cnt.append(cnt)

    print(f"#{t} {max(res_cnt)}")