# 각 좌표 별로 dfs 이용하여 구현
# 방향은 (1, -1), (1, 1), (-1, 1), (-1, -1) -> 이 순서
# 세번 바꾼 이후에는 처음 값까지 이동
# 사각형이 만들어지면 경로에 있던 요소들의 수를 결과에 저장(최대값)
# 중간에 return 조건 : 배열의 범위를 벗어났을 때, 이미 지나온 경로에 있는 값과 같은 값에 접근했을 때(방문처리)
# 모든 사각형을 탐색 후 출력
# 사각형이 완성 됐을 때만 결과 값을 비교

dir_4 = [(1, -1), (1, 1), (-1, 1), (-1, -1)]


def find_route(y, x, dr):
    global dessert_map, route, visited
    for d in range(dr, 4):
        dy, dx = dir_4[d]
        nx = x + dx
        ny = y + dy
        if 0 <= x < N and 0 <= y < N:
            if d == 3 and (ny, nx) == start_xy:
                result = max(len(route), result)
                return
            if dr < 3:
                if not visited[dessert_map[y][x]]:
                    visited[dessert_map[ny][nx]] = True
                    find_route(ny, nx, d)


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    dessert_map = [list(map(int, input().split())) for _ in range(N)]
    result = -1
    passing_len = 0
    start_xy = (0, 0)
    edge = [(0, 0), (0, N - 1), (N - 1, 0), (N - 1, N - 1)]
    for i in range(N):
        for j in range(N):
            route = []
            visited = [False] * 101
            start_xy = (i, j)
            visited[dessert_map[i][j]] = True
            find_route(i, j, 0)
