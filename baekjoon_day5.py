import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
m = int(input())
C = list(map(int, input().split()))

queue_num = deque()
result = []

for i in range(n):
    if A[i] == 0:
        queue_num.append(B[i])

for i in range(m):
    queue_num.appendleft(C[i])
    result.append(queue_num.pop())
    
print(*result,sep=" ")