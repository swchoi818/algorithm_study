n = int(input())

num_list = list(map(str, range(1, n+1)))
result = []
for i in num_list:
    cnt = i.count('3') + i.count('6') + i.count('9')
    if cnt > 0:
        result.append(("-"*cnt))
    else:
        result.append(i)
print(*result, sep=' ')