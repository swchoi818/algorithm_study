import sys

input = sys.stdin.readline

def switch_man(num):
    for i in range(switch_num):
        if (i+1)%num == 0:
            switch_list[i] = not switch_list[i]
    # print(switch_list)
def switch_girl(num):
    if switch_num/2 >= num:
        ran = num
    else:
        ran = switch_num - num
    num -= 1
    for i in range(1, ran + 1):
        if num - i < 0 or num + i >= len(switch_list):
            break
        if switch_list[num - i] == switch_list[num + i]:
            switch_list[num - i] = not switch_list[num - i]
            switch_list[num + i] = not switch_list[num + i]
        else:
            break
    switch_list[num] = not switch_list[num]
    # print(switch_list)

switch_num = int(input())

switch_list = list(map(bool,map(int,input().split())))

stud_num = int(input())

for i in range(stud_num):
    stud_info = []
    stud_info = list(map(int,input().split()))
    if stud_info[0] == 1:
        switch_man(stud_info[1])
    else :
        switch_girl(stud_info[1])

for i in range(len(switch_list)):
    if i % 20 == 0 and i >= 20:
        print()
    if switch_list[i]:
        print('1', end=' ')
    else:
        print('0', end=' ')
