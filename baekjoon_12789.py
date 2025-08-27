import sys

input = sys.stdin.readline

N = int(input())

student_list = list(map(int, input().split()))
now_num = 1
stack_list = []
i = 0
for i in student_list+[0]:
    if now_num == i:
        now_num += 1
    else:
        if stack_list:
            for j in range(len(stack_list),0,-1):
                if now_num == stack_list[j-1]:
                    stack_list.pop()
                    now_num += 1
                else:
                    break
        if i != 0:
            stack_list.append(i)
if not stack_list:
    print('Nice')
else:
    print('Sad')
