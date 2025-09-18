from collections import deque

dir_8 = [(0, -1), (0, 1), (1, 0), (-1, 0), (1, -1), (-1, 1), (1, 1), (-1, -1)]

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    mine_mtr = [list(input()) for _ in range(N)]
    cnt = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if mine_mtr[i][j] == '*' or visited[i][j]:
                continue
            for dy, dx in dir_8:
                ny = i + dy
                nx = j + dx
                if 0 <= nx < N and 0 <= ny < N:
                    if mine_mtr[ny][nx] == '*':
                        break
            else:
                visited[i][j] = True
                dq = deque()
                dq.append((i, j))
                cnt += 1
                while dq:
                    y, x = dq.popleft()
                    tmp = []
                    for dy, dx in dir_8:
                        ny = y + dy
                        nx = x + dx
                        if 0 <= nx < N and 0 <= ny < N:
                            if mine_mtr[ny][nx] == '*':
                                break
                            if not visited[ny][nx]:
                                tmp.append((ny, nx))
                    else:
                        for ny, nx in tmp:
                            visited[ny][nx] = True
                            dq.append((ny, nx))

    for i in range(N):
        for j in range(N):
            if mine_mtr[i][j] == '*' or visited[i][j]:
                continue
            cnt += 1

    print(f'#{t}', cnt)
