# 왔던 경로의 숫자를 저장하는 집합 생성
# 다시 돌아왔을 때 각 집합에 있는 값을 sum
# dfs 
# dir 0 1 이후 3 4는 정해져 있음, 방향을 바꿀 때 현재 이동한 만큼 거리를 저장하는 변수 선언 필요

def dessert_route(y, x):
    global N, dessert_mtr, dir_diag, visited, length, result, res_cnt
    for i in range(2):
        dy, dx = dir_diag[i]
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < N:
            if dessert_mtr[ny][nx] in visited:
                return
            length[i] += 1
            visited.add(dessert_mtr[ny][nx])
            dessert_route(ny, nx)
            length[i] -= 1
            visited.discard(dessert_mtr[ny][nx])

    for dx, dy in dir_diag[2:4]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < N:
            if dessert_mtr[ny][nx] in visited:
                return
            visited.add(dessert_mtr[ny][nx])
    else:
        if sum(visited) > result:
            result = sum(visited)
            print(visited)
            res_cnt = len(visited)


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    dessert_mtr = [list(map(int, input().split())) for _ in range(N)]
    visited = set()
    result = 0
    res_cnt = -1
    length = [0, 0]
    dir_diag = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
    edge = [(0, 0), (0, N - 1), (N - 1, 0), (N - 1, N - 1)]

    for i in range(N):
        for j in range(N):
            if (i, j) not in edge:
                visited = set()
                dessert_route(i, j)
    
    print(f"#{t} {res_cnt}")

