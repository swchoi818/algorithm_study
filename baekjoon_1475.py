N = input()
set_num = 0
for i in range(len(N)):
    
    if N[i] == '9' or N[i] == '6':
        cnt = (N.count('9') + N.count('6'))
        cnt = cnt - (cnt//2)
    else:
        cnt = N.count(N[i])
    if set_num < cnt:
        set_num = cnt

print(set_num)