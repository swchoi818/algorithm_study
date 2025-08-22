def dfs(selected, remain):
    global result

    if len(selected) == N // 2:
        lst_tmp = list(selected)
        synergy1 = get_synergy(lst_tmp)
        lst_tmp = list(set(remain_l) - selected)
        synergy2 = get_synergy(lst_tmp)
        result.append(abs(synergy1 - synergy2))
        return

    for i in range(len(remain)):
        selected.add(remain[i])
        dfs(selected, remain[i + 1:])
        selected.discard(remain[i])


def get_synergy(lst):
    synergy = 0
    for i in lst:
        for j in lst:
            if i == j:
                continue
            synergy += taste_list[i][j]
    return synergy


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    taste_list = [list(map(int, input().split())) for _ in range(N)]
    result = []
    remain_l = [i for i in range(N)]
    select_l = set()
    dfs(select_l, remain_l[:])
    print(f"#{t}", min(result))
