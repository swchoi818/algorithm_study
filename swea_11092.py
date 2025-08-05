T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    num_list = list(map(int, input().split()))
    
    min_index = num_list.index(min(num_list))
    max_index = n - 1 - num_list[::-1].index(max(num_list))
    
    print(f"#{test_case}",abs(max_index - min_index))