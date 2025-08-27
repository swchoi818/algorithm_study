import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    ps = input()
    stack = 0
    for i in ps:
        if i == '(':
            stack+=1
        elif i == ')':
            stack-=1
            if stack < 0:
                break
    if stack:
        print('NO')
    else:
        print('YES')