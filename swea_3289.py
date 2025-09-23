def find_set(x):
    global p_list
    if x != p_list[x]:
        p_list[x] = find_set(p_list[x])
    return p_list[x]


def union_set(x, y):
    global p_list, rank
    px = find_set(x)
    py = find_set(y)

    if px != py:
        if rank[px] > rank[py]:
            p_list[py] = px
        elif rank[px] > rank[py]:
            p_list[px] = py
        else:
            p_list[py] = px
            rank[px] += 1


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    p_list = list(range(N + 1))
    rank = [0] * (N + 1)
    cmd_list = [list(map(int, input().split())) for _ in range(M)]
    result = ''
    for cmd in cmd_list:
        if cmd[0] == 0:
            union_set(cmd[1], cmd[2])
        else:
            if find_set(cmd[1]) == find_set(cmd[2]):
                result += '1'
            else:
                result += '0'

    print(f'#{t}', result)
