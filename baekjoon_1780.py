def is_square(mtr):
    global result
    for i in mtr:
        for j in i:
            if j != mtr[0][0]:
                return False
    result[mtr[0][0] + 1] += 1
    return True


def divide(mtr):
    div3 = len(mtr) // 3
    loc = [(0, div3), (div3, div3 * 2), (div3 * 2, len(mtr))]
    for sr, er in loc:
        for sc, ec in loc:
            divided = [copy_mtr[sc:ec] for copy_mtr in mtr[sr:er]]
            if not is_square(divided):
                divide(divided)


N = int(input())

paper_mtr = [list(map(int, input().split())) for _ in range(N)]

result = [0] * 3

if not is_square(paper_mtr):
    divide(paper_mtr)

print(*result, sep='\n')
