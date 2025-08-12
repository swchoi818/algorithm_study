priority_oper = {'+' : 1, '*' : 2}

for t in range(1, 11):
    N = input()
    formulor = input()
    temp_stack = []
    result_stack = []
    for i in formulor:
        if i.isnumeric():
            result_stack.append(i)
        else:
            while temp_stack and (priority_oper[i] <= priority_oper[temp_stack[len(temp_stack) - 1]]):
                result_stack.append(temp_stack.pop())
            temp_stack.append(i)
                
    while temp_stack:
        result_stack.append(temp_stack.pop())
        
    for i in result_stack:
        if i.isnumeric():
            temp_stack.append(i)
        elif i == '+':
            temp_stack.append(int(temp_stack.pop()) + int(temp_stack.pop()))
        elif i == '*':
            temp_stack.append(int(temp_stack.pop()) * int(temp_stack.pop()))
    
    print(f"#{t} {temp_stack.pop()}")