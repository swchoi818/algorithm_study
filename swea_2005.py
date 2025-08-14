T = int(input())

for t in range(1, T + 1):
    N = int(input())
    pascal_trianle = []
    tmp_stack = []
    for i in range(1, N + 1):
        for j in range(i):
            if j == 0:
                tmp_stack.append(1)
                continue
            if j == i - 1:
                tmp_stack.append(1)
                tmp = tmp_stack[:]
                continue
            tmp_stack.append(tmp.pop() + tmp[len(tmp) - 1])
            
        pascal_trianle.append(tmp_stack)
        tmp_stack = []
        
    print(f"#{t}", *[' '.join(map(str, p)) for p in pascal_trianle], sep="\n")