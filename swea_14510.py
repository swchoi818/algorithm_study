T = int(input())

for t in range(1, T + 1):
    N = int(input())
    tree_list = list(map(int, input().split()))
    max_height = max(tree_list)
    diff_list = []
    for i in tree_list:
        if i == max_height:
            continue
        diff_list.append(max_height - i)
    day_cnt = 0
    diff_list.sort()
    while diff_list:
        if diff_list[len(diff_list) - 1] == 0:
            diff_list.pop()
            continue
        day_cnt += 1
        two_cnt = 0
        len_ele = 0
        # print(day_cnt, diff_list, (day_cnt % 2) - 2)
        for i in range(len(diff_list) - 1, -1, -1):
            if diff_list[i] == 0:
                continue
            len_ele += 1
            if day_cnt % 2 == 1:
                if diff_list[i] % 2 == 1:
                    diff_list[i] -= 1
                    break
                else :
                    two_cnt += 1
            else:
                if diff_list[i] >= 2:
                    diff_list[i] -= 2
                    break
        else:
            if day_cnt % 2 == 1 and diff_list and (len_ele == two_cnt > 1 or diff_list[len(diff_list) - 1] > 2):
                diff_list[len(diff_list) - 1] -= 1

    print(f"#{t} {day_cnt}")
