
T = int(input())

for i in range(T):
    N = int(input())
    str_card = input()
    a = [0 for _ in range(10)]
    for j in str_card:
        a[int(j)] += 1
    # max_num = 0
    # result = 0
    # for j in range(10):
    #     if max_num <= a[j]:
    #         max_num = a[j]
    #         result = j
    
    max_num = max(a)
    result = 9 - a[::-1].index(max_num)
    
    print(f"#{i+1} {result} {a[result]}")
    
    