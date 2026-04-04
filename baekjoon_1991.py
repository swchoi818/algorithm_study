import sys
from collections import defaultdict

input = sys.stdin.readline

def pre_order(node):
    if node == '.':
        return
    pre_result.append(node)
    pre_order(bin_tree[node][0])
    pre_order(bin_tree[node][1])

def in_order(node):
    if node == '.':
        return
    in_order(bin_tree[node][0])
    in_result.append(node)
    in_order(bin_tree[node][1])

def post_order(node):
    if node == '.':
        return
    post_order(bin_tree[node][0])
    post_order(bin_tree[node][1])
    post_result.append(node)

pre_result = []
in_result = []
post_result = []

N = int(input())

bin_tree = defaultdict(list)

for _ in range(N):
    p, left, right = map(str, input().split())
    bin_tree[p] = [left, right]

pre_order('A')
in_order('A')
post_order('A')

print(''.join(pre_result))
print(''.join(in_result))
print(''.join(post_result))




