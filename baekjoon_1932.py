# from collections import deque
import sys

input = sys.stdin.readline

# #dfs 활용
# def dfs(y, x, current_num):
#     global result, num_triangle
#     if visited[y][x] >= current_num:
#         return
#     ny = y + 1
#     if ny >= N:
#         result = max(current_num, result)
#         return
#     for nx in range(x, x + 2):
#         dfs(ny, nx, current_num + num_triangle[ny][nx])


N = int(input())

num_triangle = [list(map(int, input().split())) for _ in range(N)]
sum_list = [[0] * i for i in range(1, N + 1)]

sum_list[0][0] = num_triangle[0][0]

# dfs(0, 0, num_triangle[0][0])

# #bfs 활용
# dq = deque()
# dq.append((0, 0, num_triangle[0][0]))
# result = 0

# while dq:
#     y, x, sum_num = dq.popleft()
#     ny = y + 1
#     if ny >= N:
#         result = max(sum_num, result)
#         continue
#
#     for nx in range(x, x + 2):
#         nest_sum = (sum_num + num_triangle[ny][nx])
#         if nest_sum <= visited[ny][nx]:
#             continue
#         visited[ny][nx] = nest_sum
#         dq.append((ny, nx, nest_sum))

# DP
for i in range(1, N):
    for j in range(i + 1):
        if j == 0:
            sum_list[i][j] = num_triangle[i][j] + sum_list[i - 1][j]
        elif j == i:
            sum_list[i][j] = num_triangle[i][j] + sum_list[i - 1][j - 1]
        else:
            sum_list[i][j] = max(
                (num_triangle[i][j] + sum_list[i - 1][j - 1]),
                (num_triangle[i][j] + sum_list[i - 1][j]),
            )

print(max(sum_list[N - 1]))
