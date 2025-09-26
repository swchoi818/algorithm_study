def make_binary_str():
    graph = [[A, B], [C, D]]
    if B == 0 and C == 0 and A and D:
        return 'impossible'
    if abs(B - C) > 1:
        return 'impossible'
    if B == C:
        if A + B:
            node = 0
        elif C + D:
            node = 1
    elif B - C == 1:
        node = 0
    elif C - B == 1:
        node = 1

    return str(node) + dfs(node, node, graph)


def dfs(st, ed, graph):
    if graph[st][ed] != 0:
        graph[st][ed] -= 1
        result = str(st)
    elif graph[st][1 - ed] != 0:
        ed = 1 - ed
        graph[st][ed] -= 1
        result = str(ed)
    else:
        return ''
    result += dfs(ed, ed, graph)
    return result


T = int(input())

for t in range(1, T + 1):
    A, B, C, D = map(int, input().split())
    print(f'#{t}', make_binary_str())