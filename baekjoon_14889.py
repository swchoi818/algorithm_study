def dfs(selected, remain):
    global result
    if len(selected) == N // 2:
        lst_tmp = list(selected)
        ability1 = get_team_ability(lst_tmp)
        lst_tmp = list(set(remain_l) - selected)
        ability2 = get_team_ability(lst_tmp)
        result.append(abs(ability1 - ability2))
        return

    for i in range(len(remain)):
        selected.add(remain[i])
        dfs(selected, remain[i + 1:])
        selected.discard(remain[i])


def get_team_ability(lst):
    ability = 0
    for i in lst:
        for j in lst:
            if i == j:
                continue
            ability += player_mtr[i][j]
    return ability


N = int(input())
player_mtr = [list(map(int, input().split())) for _ in range(N)]
result = []
remain_l = [i for i in range(N)]
select_l = set()
dfs(select_l, remain_l[:])

print(min(result))
