def is_square(mtr):
    is_one = True
    is_zero = True
    for i in mtr:
        for j in i:
            if j == '0':
                is_one = False
            elif j == '1':
                is_zero = False
    if is_one:
        return 1
    elif is_zero:
        return 0
    return -1

def make_quadtree(mtr):
    global quadtree
    harf_len = len(mtr) // 2
    quadrant = [(0, harf_len), (harf_len, len(mtr))]
    for sh, eh in quadrant:
        for sw, ew in quadrant:
            divide_mtr = [copy_mtr[sw:ew] for copy_mtr in mtr[sh:eh]]
            comp = is_square(divide_mtr)
            if comp == -1:
                quadtree.append('(')
                make_quadtree(divide_mtr)
                quadtree.append(')')
            elif comp == 1:
                quadtree.append('1')
            else:
                quadtree.append('0')


N = int(input())

img_mtr = [list(input()) for _ in range(N)]

quadtree = []
comp = is_square(img_mtr)
if comp == -1:
    quadtree.append('(')
    make_quadtree(img_mtr)
    quadtree.append(')')
    print(''.join(quadtree))
else:
    print(comp)
