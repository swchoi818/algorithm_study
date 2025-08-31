# 블럭의 종류 5개 리스트 안에 딕셔너릴로 생성하여 현재 방향을 key, value로 바뀌는 방향 표시
# -1 만나면 종료, 시작 위치로 돌아오면 종료
# 배열의 바깥부분을 5로 설정
# 방향이 바뀔 때마다 score++

dir_4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]

block_list = [[None],{(-1, 0) : (1, 0), (1, 0) : (0, 1), (0, -1): (-1, 0), (0, 1) : (0, -1)},
              {(-1, 0) : (0, 1), (1, 0) : (-1, 0), (0, -1) : (1, 0), (0, 1): (0, -1)},
              {(-1, 0) : (0, -1), (1, 0) : (-1, 0), (0, -1) : (0, 1), (0, 1): (1, 0)},
              {(-1, 0) : (1, 0), (1, 0) : (0, -1), (0, -1): (0, 1), (0, 1) : (1, 0)},
              {(-1, 0) : (1, 0), (1, 0) : (-1, 0), (0, -1): (0, 1), (0, 1) : (0, -1)}]



def warp(loc, num):
    if worm_hole[num][0] == loc:
        return worm_hole[num][1]
    return worm_hole[num][0]


def start_pinball(st_y, st_x, st_dir):
    global score
    dy, dx = st_dir
    ny , nx = st_y, st_x
    while True:
        ny += dy
        nx += dx
        if (ny, nx) == (st_y, st_x) or game_board[ny][nx] == -1:
            break
        if 0 < game_board[ny][nx] <= 5:
            score += 1
            dy, dx = block_list[game_board[ny][nx]][(dy, dx)]
        elif 5 < game_board[ny][nx]:
            ny, nx = warp((ny, nx), game_board[ny][nx])


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    game_board = [[5] * (N + 2)]
    worm_hole = {}
    for _ in range(N):
        game_board.append([5] + list(map(int, input().split())) + [5])
    game_board.append([5] * (N + 2))
    score = 0
    result = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if game_board[i][j] > 5:
                if worm_hole.get(game_board[i][j]):
                    worm_hole[game_board[i][j]].append((i, j))
                else:
                    worm_hole[game_board[i][j]] = [(i, j)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if game_board[i][j] != 0:
                continue
            for dy, dx in dir_4:
                score = 0
                start_pinball(i, j, (dy, dx))
                result = max(result, score)

    print(f"#{t}", result)
