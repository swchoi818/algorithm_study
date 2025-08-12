for t in range(1, 11):
    N = input()
    formulor = input()
    temp = ''
    result_stack = []
    for i in formulor:
        if i.isnumeric():
            result_stack.append(i)
        else:
            if temp:
                result_stack.append(temp)
                temp = ''
            temp = i
    result_stack.append(temp)
    oper_stack = []
    for i in result_stack:
        if i.isnumeric():
            oper_stack.append(i)
        else:
            oper_stack.append(int(oper_stack.pop()) + int(oper_stack.pop()))
    
    print(f"#{t} {oper_stack.pop()}")