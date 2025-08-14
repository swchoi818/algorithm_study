from collections import deque

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    tree_list = list(map(int, input().split()))
    max_height = max(tree_list)
    diff_deq = deque()
    diff_list = []
    for i in tree_list:
        diff_list.append(max_height - i)
    day_cnt = 0
    while diff_list:
        if diff_list[len(diff_list) - 1] == 0:
            diff_list.pop()
            continue
        day_cnt += 1
        for i in range(len(diff_list) - 1, -1, -1):
            if diff_list[i] == 0:
                continue
            if day_cnt % 2 == 1:
                if diff_list[i] != 2:
                    diff_list[i] -= 1
                    break
            else:
                if diff_list[i] != 1:
                    diff_list[i] -= 2
                    break
        else:
            if diff_list and len(diff_list) != 1:
                diff_list[len(diff_list) - 1] -= 1

    print(f"#{t} {day_cnt}")




