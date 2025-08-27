import sys

input = sys.stdin.readline

while True:
    ps = input()
    if ps == '.\n':
        exit()
    stack = []
    result = True
    for i in ps:
        if (i == '(') or (i == '['):
            stack.append(i)
        elif i == ')':
            if not stack or stack.pop() != '(':
                result = False
                break
        elif i == ']':
            if not stack or stack.pop() != '[':
                result = False
                break    
    if result and not stack:
        print('yes')
    else:
        print('no')