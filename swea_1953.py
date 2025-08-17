# bfs? 

tunnel_type = {1 : ((1, 0), (-1, 0), (0, 1), (0, -1)), 2 : ((-1, 0), (1, 0)), 3 : ((0, -1), (0, 1)), 4 : ((-1, 0), (0, 1)), 5 : ((1, 0), (0, 1)), 6 : ((1, 0), (0, -1)), 7 : ((-1, 0), (0, -1))}

def search_criminal(locate, time):
    global tunnel_mtr, N, M, L, visited
    if time > L:
        return
    next_locate = []
    for y, x in locate:
        visited.add((y, x))
        for dy, dx in tunnel_type[tunnel_mtr[y][x]]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < M and 0 <= ny < N and (ny, nx) not in visited and tunnel_mtr[ny][nx] != 0 and (-dy, -dx) in tunnel_type[tunnel_mtr[ny][nx]]:
                next_locate.append((ny, nx))
    search_criminal(next_locate, time + 1)


T = int(input())

for t in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())

    visited = set()

    tunnel_mtr = [list(map(int, input().split())) for _ in range(N)]

    search_criminal([(R, C)], 1)

    print(f"#{t} {len(visited)}")
