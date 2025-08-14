dir_tpl = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))

reverse_color = {2 : 1, 1 : 2}

T = int(input())

N = M = 0

othello_mtr = []

def othello_set(sx, sy, clr):
    othello_mtr[sy][sx] = clr
    for dx, dy in dir_tpl:
        length = 1
        while True:
            x = sx + dx * length
            y = sy + dy * length
            if (not ((0 <= x < N) and (0 <= y < N))) or othello_mtr[y][x] == 0:
                break
            elif othello_mtr[y][x] == clr:
                ex = x
                ey = y
                for i in range(max(abs(x-sx), abs(y-sy)) - 1):
                    ex -= dx
                    ey -= dy
                    othello_mtr[ey][ex] = reverse_color[othello_mtr[ey][ex]]
                break
            length += 1

for t in range(1, T+1):
    N, M = map(int, input().split())

    othello_mtr = [[0]*N for _ in range(N)]

    othello_mtr[N//2 - 1][N//2 - 1] = 2
    othello_mtr[N//2][N//2] = 2
    othello_mtr[N//2][N//2 - 1] = 1
    othello_mtr[N//2 - 1][N//2] = 1
    
    b_cnt = 0
    w_cnt = 0

    for _ in range(M):
        x, y, clr = map(int, input().split())
        othello_set(x-1, y-1, clr)
        
    for i in range(N):
        for j in range(N):
            if othello_mtr[i][j] == 1:
                b_cnt += 1
            elif othello_mtr[i][j] == 2:
                w_cnt += 1

    print(f"#{t} {b_cnt} {w_cnt}")