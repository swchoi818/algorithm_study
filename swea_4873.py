T = int(input())
 
for t in range(1, T + 1):
    str_list = list(input())
    stack_list = []
    for i in str_list:
        if (len(stack_list) != 0) and (stack_list[len(stack_list) - 1] == i):
            stack_list.pop()
        else:
            stack_list.append(i)
          
     
    print(f"#{t} {len(stack_list)}")
    