# 백트래킹, 델타 탐색 이용
# fine_trail -> 현재 위치와 길이, 공사 여부(K를 받아서 공사를 진행하면 K를 0으로 변경)를 매개변수로 받음
# 결과는 전역 변수로 선언, 갈 곳이 없을 때 길이를 결과와 비교하여 큰값을 결과에 저장하고 리턴

dir_4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]

result = 0

map_mtr = []

N = 0

def find_trail(x, y, k, visited):
    global result
    is_end = True
    for dx, dy in dir_4:
        nx = x - dx
        ny = y - dy
        if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
            if map_mtr[ny][nx] < map_mtr[y][x]:
                is_end = False
                visited.add((nx, ny))
                find_trail(nx, ny, k, visited)
                visited.remove((nx, ny))
            elif k != 0:
                for i in range(1, k + 1):
                    if map_mtr[ny][nx] - i < map_mtr[y][x]:
                        is_end = False
                        map_mtr[ny][nx] -= i
                        visited.add((nx, ny))
                        find_trail(nx, ny, 0, visited)
                        visited.remove((nx, ny))
                        map_mtr[ny][nx] += i
                        break
    if is_end:
        result = max(result, len(list(visited)))

T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    
    result = 0

    map_mtr = [list(map(int, input().split())) for _ in range(N)]

    most_high = max(map(max, map_mtr))

    for i in range(N):
        for j in range(N):
            if map_mtr[i][j] == most_high:
                visited = {(j, i)}
                find_trail(j, i, K, visited)

    print(f"#{t} {result}")