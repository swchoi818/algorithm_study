from collections import deque

T = int(input())

dir_4 = [(0, 1), (0, -1), (-1, 0), (1, 0)]

for t in range(1, T + 1):
    N = int(input())
    room_mtr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    cnt_mtr = [[0] * N for _ in range(N)]
    deq = deque()
    result = [0, 0]
    for r in range(N):
        for c in range(N):
            if visited[r][c]:
                continue
            cnt = 0
            deq.append((r, c, 1))
            while deq:
                y, x, cnt = deq.popleft()
                if visited[y][x]:
                    cnt_mtr[r][c] = cnt - 1 + cnt_mtr[y][x]
                    break
                visited[y][x] = True
                for dx, dy in dir_4:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < N and 0 <= ny < N and room_mtr[ny][nx] == room_mtr[y][x] + 1:
                        deq.append((ny, nx, cnt + 1))
                        break
                else:
                    cnt_mtr[r][c] = cnt
            visited[r][c] = True
            if result[1] < cnt_mtr[r][c]:
                result = [room_mtr[r][c], cnt_mtr[r][c]]
            elif result[1] == cnt_mtr[r][c]:
                result[0] = min(result[0], room_mtr[r][c])

    print(f"#{t}", *result)