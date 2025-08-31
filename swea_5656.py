from collections import deque

from copy import deepcopy

dir_4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def cnt_block(blk_mtr):
    cnt = 0
    for w in range(W):
        for h in range(H - 1, -1, -1):
            if blk_mtr[h][w] == 0:
                continue
            cnt += 1
    return cnt


def drop_block(bck_mtr):
    for r in range(1, H):
        for c in range(W):
            if bck_mtr[r][c] == 0:
                ur = r
                while bck_mtr[ur - 1][c] != 0:
                    bck_mtr[ur][c] = bck_mtr[ur - 1][c]
                    bck_mtr[ur - 1][c] = 0
                    ur -= 1
                    if ur <= 0:
                        break


def bfs(bx, bck_mtr):
    blk_que = deque()
    for y in range(H):
        if bck_mtr[y][bx] >= 1:
            blk_que.append((y, bx))
            break
    while blk_que:
        y, x = blk_que.popleft()
        for dy, dx in dir_4:
            ny = y
            nx = x
            for i in range(bck_mtr[y][x] - 1):
                ny += dy
                nx += dx
                if not (0 <= ny < H and 0 <= nx < W):
                    break
                if bck_mtr[ny][nx] == 1:
                    bck_mtr[ny][nx] = 0
                    continue
                if bck_mtr[ny][nx] > 1:
                    blk_que.append((ny, nx))
        bck_mtr[y][x] = 0
    drop_block(bck_mtr)


def dfs(selected, remain):
    global N, result, block_mtr, is_end
    if is_end:
        return
    if len(selected) == N:
        tmp_blk = deepcopy(block_mtr)
        for bx in selected:
            bfs(bx,tmp_blk)
        result.append(cnt_block(tmp_blk))
        if cnt_block(tmp_blk) == 0:
            is_end = True
        return
    for i in range(len(remain)):
        selected.append(remain[i])
        dfs(selected, remain)
        selected.pop()


T = int(input())

for t in range(1, T + 1):
    N, W, H = map(int, input().split())
    result = []
    is_end = False
    block_mtr = [list(map(int, input().split())) for _ in range(H)]

    dfs([], list(range(W)))

    print(f"#{t}", min(result))
