def count_sub(root):
    global result, btree
    if not btree.get(root):
        return
    result += len(btree[root])
    for i in btree[root]:
        count_sub(i)


def dfs(a, b):
    visited[a] = True
    visited[b] = True
    if a == b:
        return a
    if p_dict[a] != a and visited[p_dict[a]]:
        return p_dict[a]
    elif p_dict[b] != b and visited[p_dict[b]]:
        return p_dict[b]

    return dfs(p_dict[a], p_dict[b])


T = int(input())

for t in range(1, T + 1):
    V, E, v1, v2 = map(int, input().split())
    result = 1
    btree = {}
    p_dict = [0] * (V + 1)
    p_dict[1] = 1
    visited = [False] * (V + 1)
    node = list(map(int, input().split()))
    for i in range(0, E * 2, 2):
        if btree.get(node[i]):
            btree[node[i]].append(node[i + 1])
        else:
            btree[node[i]] = [node[i + 1]]

        p_dict[node[i + 1]] = node[i]
    common = dfs(v1, v2)
    count_sub(common)

    print(f"#{t}", common, result)
