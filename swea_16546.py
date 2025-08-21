T = int(input())


def check_trp_run(select1, select2):
    for i in (select1, select2):
        is_triplet = True
        is_run = True
        for j in range(1, 3):
            if i[j - 1] != i[j] - 1:
                is_triplet = False
            if i[j - 1] != i[j]:
                is_run = False
        if not (is_run or is_triplet):
            return False
    else:
        return True


def check_baby_gin(selected, remain):
    global is_baby_gin
    if is_baby_gin:
        return
    if len(selected) == 3:
        if check_trp_run(sorted(selected), sorted(remain)):
            is_baby_gin = True
        return

    for i in range(len(remain)):
        tmp_select = selected + [remain[i]]
        tmp_remain = remain[:i] + remain[i + 1:]
        check_baby_gin(tmp_select, tmp_remain)


for t in range(1, T + 1):
    card_list = list(map(int, list(input().strip())))
    is_baby_gin = False
    check_baby_gin([], card_list)
    if is_baby_gin:
        print(f'#{t} true')
    else:
        print(f'#{t} false')
