class Tree:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


def inorder(node):
    global tree, result
    if tree[node].left:
        inorder(tree[node].left)
    result += tree[node].value
    if tree[node].right:
        inorder(tree[node].right)


for t in range(1, 11):
    N = int(input())
    tree = [None] + [[] for _ in range(N)]
    result = ''
    for _ in range(N):
        tmp = list(map(str, input().split()))
        if len(tmp) == 4:
            tree[int(tmp[0])] = Tree(tmp[1], int(tmp[2]), int(tmp[3]))
        elif len(tmp) == 3:
            tree[int(tmp[0])] = Tree(tmp[1], int(tmp[2]))
        elif len(tmp) == 2:
            tree[int(tmp[0])] = Tree(tmp[1])

    inorder(1)

    print(f'#{t}', result)
