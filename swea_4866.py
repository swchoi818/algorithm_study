T = int(input())

for t in range(1, T + 1):
    str_list = input()
    stack_char = []
    result = 1
    for i in str_list:
        if i == '(' or i == '{':
            stack_char.append(i)
        try:
            if i == ')' and stack_char.pop() != '(':
                result = 0
                break
            elif i == '}' and stack_char.pop() != '{':
                result = 0
                break
        except:
            result = 0
            break

    if stack_char:
        result = 0

    print(f"#{t} {result}")
