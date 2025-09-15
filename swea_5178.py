class Tree:
    def __init__(self, v):
        self.left = v * 2
        self.right = v * 2 + 1
        self.value = None
        self.v = v


def sum_child(node):
    global btree
    if not btree.get(node):
        return 0
    if btree[node].value:
        return btree[node].value
    btree[node].value = sum_child(btree[node].left) + sum_child(btree[node].right)
    return btree[node].value


T = int(input())

for t in range(1 , T + 1):
    N, M, L = map(int, input().split())
    btree = {i: Tree(i) for i in range(1, N + 1)}
    for _ in range(M):
        key, value = map(int, input().split())
        btree[key].value = value

    sum_child(1)

    print(f'#{t}', btree[L].value)