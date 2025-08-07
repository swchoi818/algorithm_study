import copy

x_dir = (-1, 1)


def count_length(now_x, mtr2):
    now_y = 0
    cnt = 0
    while now_y < 100:
        for dx in x_dir:
            x = now_x + dx
            if 0 <= x < 100:
                if mtr2[now_y][x] == 1:
                    mtr2[now_y][now_x] = 0
                    now_x = x
                    cnt += 1
                    break
        else:
            now_y += 1   
    return cnt


for test_case in range(1, 11):
    input()
    mtr = [list(map(int, input().split())) for _ in range(100)]
    min_num = 0
    min_point = 0
    for i in range(100):
        if mtr[0][i] == 1:
            temp = count_length(i, copy.deepcopy(mtr))
            if min_num == 0:
                min_num = temp
                min_point = i
            elif min_num >= temp:
                min_num = temp
                min_point = i
    print(f"#{test_case}", min_point)