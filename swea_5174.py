def count_sub(root):
    global result, btree
    if not btree.get(root):
        return
    result += len(btree[root])
    for i in btree[root]:
        count_sub(i)


T = int(input())

for t in range(1, T + 1):
    E, N = map(int, input().split())
    result = 1
    btree = {}
    node = list(map(int, input().split()))
    for i in range(0, E * 2, 2):
        if btree.get(node[i]):
            btree[node[i]].append(node[i + 1])
        else:
            btree[node[i]] = [node[i + 1]]
    count_sub(N)

    print(f"#{t}", result)