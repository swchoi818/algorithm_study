import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

def dfs(n):
    for j in graph[n]:
        if parents[j]:
            continue
        parents[j] = n
        dfs(j)
    
    
N = int(input())

nodes = [list(map(int, input().split())) for _ in range(N - 1)]
graph = defaultdict(list)

for n1, n2 in nodes:
    graph[n1].append(n2)
    graph[n2].append(n1)

parents = [0] * (N + 1)

dfs(1)

print(*parents[2:], sep="\n")
