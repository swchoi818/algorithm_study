for test_case in range(1, 11):
    input()
    num_list = []
    for _ in range(100):
        num_list.append(list(map(int,input().split())))
    num_sum = 0
    num_sum2 = 0
    max_sum = 0
    for i in num_list:
        num_sum = sum(i)
        max_sum = max(max_sum, num_sum)
        num_sum = 0
    for i in range(100):
        for j in range(100):
            num_sum += num_list[j][i]
            max_sum = max(max_sum, num_sum)
        num_sum = 0
    for i in range(100):
        num_sum += num_list[i][i]
        num_sum2 += num_list[i][99 - i]
    max_sum = max(max_sum, num_sum, num_sum2)
    num_sum = 0
    num_sum2 = 0
    print(f"#{test_case}", max_sum)