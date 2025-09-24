expression = input() + '_'

result_list = ['']
is_plus = False
p = 0
for n in expression:
    if n.isnumeric():
        result_list[p] += n
    else:
        if is_plus:
            result_list[p - 1] = str(int(result_list[p - 1]) + int(result_list.pop()))
            is_plus = False
            p -= 1
        if n == '+':
            is_plus = True
        if n != '_':
            result_list.append('')
            p += 1

result = int(result_list[0])
for i in range(1, len(result_list)):
    result -= int(result_list[i])

print(result)