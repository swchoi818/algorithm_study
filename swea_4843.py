T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    num_list = list(map(int, input().split()))
    
    
    num_list.sort()
    result = []
    
    for i in range(5):
        result.append(num_list[::-1][i])
        result.append(num_list[i])
    print(f"#{test_case}",*result,sep=' ')
    