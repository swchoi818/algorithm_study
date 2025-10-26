import sys

def dfs(selected, remained):
    global result
    if len(selected) == M:
        result.append(''.join(selected))
        return
    for i in range(len(remained)):
        selected.append(remained[i])
        dfs(selected, remained[:i] + remained[i+1:])
        selected.pop()


input = sys.stdin.readline

N, M = map(int, input().split())
result = []
num_list = list(map(int, input().split()))

dfs([], num_list)

for r in result:
    print(*r)