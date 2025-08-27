import sys

input = sys.stdin.readline

stack_list = []

K = int(input())

for _ in range(K):
    N = int(input())
    if N == 0:
        stack_list.pop()
    else:
        stack_list.append(N)
    
print(sum(map(int,stack_list)))