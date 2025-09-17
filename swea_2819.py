dir_4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(locate, now_str):
    global cnt, mtr, visited
    if len(now_str) == 7:
        if now_str not in visited:
            visited.add(now_str)
            cnt += 1
        return
    y, x = locate
    for dy, dx in dir_4:
        ny = y + dy
        nx = x + dx
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs((ny, nx), now_str + mtr[ny][nx])


T = int(input())
for t in range(1, T + 1):
    mtr = [list(map(str, input().split())) for _ in range(4)]
    cnt = 0
    visited = set()

    for i in range(4):
        for j in range(4):
            dfs((i, j), mtr[i][j])

    print(f'#{t}', cnt)
