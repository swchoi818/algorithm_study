# dir_4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#
#
# def dfs(locate):
#     global result, maze_mtr
#     y, x = locate
#     if maze_mtr[y][x] == '3' or result == '1':
#         result = 1
#         return
#     maze_mtr[y][x] = '1'
#     for dy, dx in dir_4:
#         ny = y + dy
#         nx = x + dx
#         if 0 <= nx < 16 and 0 <= ny < 16 and maze_mtr[ny][nx] != '1':
#             dfs((ny, nx))
#
#
# for t in range(1, 11):
#     input()
#     maze_mtr = [list(input()) for _ in range(16)]
#     result = 0
#     for i in range(16):
#         for j in range(16):
#             if maze_mtr[i][j] == '2':
#                 dfs((i, j))
#                 break
#
#     print(f'#{t}', result)

from collections import deque

dir_4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for t in range(1, 11):
    input()
    maze_mtr = [list(input()) for _ in range(16)]
    result = 0
    dq = deque()
    for i in range(16):
        for j in range(16):
            if maze_mtr[i][j] == '2':
                dq.append((i, j))
                break
    while dq:
        y, x = dq.popleft()
        if maze_mtr[y][x] == '3':
            result = 1
            break
        maze_mtr[y][x] = '1'
        for dy, dx in dir_4:
            ny = y + dy
            nx = x + dx
            if 0 <= nx < 16 and 0 <= ny < 16 and maze_mtr[ny][nx] != '1':
                dq.append((ny, nx))

    print(f'#{t}', result)
