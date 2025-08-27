import sys

input = sys.stdin.readline
n = int(input())
X = list(map(int, input().split()))
Xs = sorted(set(X))
rank = {v: i for i, v in enumerate(Xs)}
Xs.sort()
result = []

for i in range(n):
    result.append(rank[X[i]])

print(*result,sep=" ")