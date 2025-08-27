N, M = map(int,input().split())

A = set()
for _ in range(N):
    A.add(input())

B = set()
for _ in range(M):
    B.add(input())
print(len(A&B))
print(*sorted(A&B), sep='\n')