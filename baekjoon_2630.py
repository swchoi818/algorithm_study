def is_square(square):
    cnt = 0
    for i in square:
        cnt += sum(i)
    if cnt == len(square) ** 2 or cnt == 0:
        return square[0][0]
    else:
        return -1


def divide_paper(paper):
    global result
    half_len = len(paper) // 2
    quadrant = [(0, half_len), (half_len, len(paper))]
    div_paper = [[[0] * half_len for _ in range(half_len)] for _ in range(4)]
    qi = 0
    for rst, red in quadrant:
        for cst, ced in quadrant:
            div_paper[qi] = [paper[i][cst:ced] for i in range(rst, red)]
            qi += 1
    for i in range(4):
        color = is_square(div_paper[i])
        if color != -1:
            result[color] += 1
            continue
        n_paper = [copy_mtr[:] for copy_mtr in div_paper[i]]
        divide_paper(n_paper)


N = int(input())

paper_mtr = [list(map(int, input().split())) for _ in range(N)]

result = [0, 0]
color = is_square(paper_mtr)
if color == -1:
    divide_paper(paper_mtr)
else:
    result[color] += 1

print(*result, sep='\n')
