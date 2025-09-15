class Tree:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def operater(node):
    global tree
    if tree[node].value.isnumeric():
        return int(tree[node].value)
    elif tree[node].value == '*':
        return operater(tree[node].left) * operater(tree[node].right)
    elif tree[node].value == '/':
        return operater(tree[node].left) // operater(tree[node].right)
    elif tree[node].value == '-':
        return operater(tree[node].left) - operater(tree[node].right)
    elif tree[node].value == '+':
        return operater(tree[node].left) + operater(tree[node].right)


for t in range(1, 11):
    N = int(input())
    tree = {}
    for _ in range(N):
        tmp = list(map(str, input().split()))
        if len(tmp) == 4:
            tree[tmp[0]] = Tree(tmp[1], tmp[2], tmp[3])
        else:
            tree[tmp[0]] = Tree(tmp[1], None, None)

    print(f'#{t}',operater('1'))