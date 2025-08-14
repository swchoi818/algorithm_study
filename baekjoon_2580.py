sudoku_mtr = [list(map(int, input().split())) for _ in range(9)]

result_mtr = []

is_row = [[False]*9 for _ in range(9)]
is_column = [[False]*9 for _ in range(9)]
is_box = [[False]*9 for _ in range(9)]


def box_index(x, y):
    return x//3 * 3 + y//3


for i in range(9):
    for j in range(9):
        if sudoku_mtr[i][j]:
            is_row[i][sudoku_mtr[i][j] - 1] = True
            is_column[j][sudoku_mtr[i][j] - 1] = True
            is_box[box_index(i, j)][sudoku_mtr[i][j] - 1] = True


def back_tracking(i, j):
    if i == 9:
        for x in sudoku_mtr:
            print(*x)
        exit(0)

    if sudoku_mtr[i][j]:
        back_tracking(i + (j + 1) // 9, (j + 1) % 9)
        return

    for k in range(9):
        if is_row[i][k] or is_column[j][k] or is_box[box_index(i, j)][k]:
            continue
        sudoku_mtr[i][j] = k + 1
        is_row[i][k] = is_column[j][k] = is_box[box_index(i, j)][k] = True
        back_tracking(i + (j + 1) // 9, (j + 1) % 9)
        sudoku_mtr[i][j] = 0
        is_row[i][k] = is_column[j][k] = is_box[box_index(i, j)][k] = False    

back_tracking(0, 0)