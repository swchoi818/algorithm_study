def pre_order(node):
    global result, btree_dict
    if not node:
        return
    result[0].append(node)
    pre_order(btree_dict[node].left)
    pre_order(btree_dict[node].right)


def in_order(node):
    global result, btree_dict
    if not node:
        return
    in_order(btree_dict[node].left)
    result[1].append(node)
    in_order(btree_dict[node].right)


def post_order(node):
    global result, btree_dict
    if not node:
        return
    post_order(btree_dict[node].left)
    post_order(btree_dict[node].right)
    result[2].append(node)


class Tree:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.v = v

    def connect_child(self, child):
        if self.left:
            self.right = child
        else:
            self.left = child


V = int(input())

node = list(map(int, input().split()))
btree_dict = {i: Tree(i) for i in range(1, V + 1)}
result = [[] for _ in range(3)]

for i in range(0, (V - 1) * 2, 2):
    btree_dict[node[i]].connect_child(node[i + 1])

pre_order(1)
in_order(1)
post_order(1)

print(*result[0])
print(*result[1])
print(*result[2])
