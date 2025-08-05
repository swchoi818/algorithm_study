T = int(input())

for test_case in range(1, T + 1):
    input()
    boxs_list = list(map(int, input().split()))
    fall_cnt = 0

    for i in boxs_list:
        cnt = 0
        for j in boxs_list[boxs_list.index(i)+1:]:       
            if i > j:
                cnt += 1
        fall_cnt = max(fall_cnt, cnt)
    
    print(f"#{test_case} {fall_cnt}")