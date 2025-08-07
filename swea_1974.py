T = int(input())
sdoku_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
for test_case in range(1, T + 1):
    sdoku_mtr = [list(map(int, input().split())) for _ in range(9)]
    sdoku_mtr_turn = list(zip(*sdoku_mtr))
    is_sdoku = True
    temp1 = set()
    temp2 = set()
    for i in range(9):
        temp1 = sdoku_set - set(sdoku_mtr[i])
        temp2 = sdoku_set - set(sdoku_mtr_turn[i])
        if len(temp1) != 0 or len(temp2) != 0:
            is_sdoku = False
            break
    for i in range(0, 9, 3):
        for j in range(9):
            temp1 = temp1.union(set(sdoku_mtr[j][i:i+3]))
            if j%3 == 2:                
                temp1 = sdoku_set - temp1
                if len(temp1) != 0:
                    is_sdoku = False
                    break
                temp1 = set()
        if not is_sdoku:
            break

    print(f"#{test_case}", int(is_sdoku))
            
