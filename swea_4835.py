T = int(input())
 
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    result = list(map(int, input().split()))
    max_sum = sum(result[0:M])
    min_sum = sum(result[0:M])
     
    for i in range(1, len(result) - M + 1):
        temp = sum(result[i:i+M])
        max_sum = max(max_sum, temp)
        min_sum = min(min_sum, temp)
             
    print(f"#{test_case}",max_sum - min_sum)