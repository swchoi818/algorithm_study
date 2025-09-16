import sys

sys.setrecursionlimit(10 ** 9)


def pre_to_post(st, end):
    if st > end:
        return
    root = pre_order[st]
    right_sub_root = end + 1
    for i in range(st + 1, end + 1):
        if pre_order[i] > root:
            right_sub_root = i
            break
    pre_to_post(st + 1, right_sub_root - 1)
    pre_to_post(right_sub_root, end)
    print(root)


pre_order = []

while True:
    try:
        tmp = input()
        if not tmp:
            break
        pre_order.append(int(tmp))
    except EOFError:
        break

pre_to_post(0, len(pre_order) - 1)
