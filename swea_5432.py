T = int(input())

for t in range(1, T + 1):
    steel_stick = input()
    tmp = ''
    steel_cnt = 0
    result = 0
    for i in steel_stick:
        if i == '(':
            steel_cnt += 1
        elif i == ')':
            steel_cnt -= 1
            if tmp == '(':
                result += steel_cnt
            else:
                result += 1
        tmp = i
    
    print(f"#{t} {result}")