T = int(input())

res_dict = {False : "NO", True : "YES"}
dirn = [(1, 1), (1, -1)]

def cnt_o(o_list, i, j):   
    cnt = 1
    cnt2 = 1
    for k in range(1, 5):
        x = j + k
        y = i + k
        if 0 <= x < n and o_list[i][x] == 'o':
            cnt += 1
        if 0 <= y < n and o_list[y][j] == 'o':
            cnt2 += 1
        if cnt == 5 or cnt2 == 5:
            return True
    return False
    
def diagonal_cnt(o_list, i, j):
    for k, l in dirn:
        cnt = 1
        for m in range(1, 5):
            x = j + k * m
            y = i + l * m
            if 0 <= x < n and 0 <= y < n and o_list[y][x] == 'o':
                cnt += 1
            if cnt == 5:
                return True
    return False

for t in range(1, T + 1):
    n = int(input())
    omok_list = [list(input()) for _ in range(n)]
    result = False
    
    for i in range(n):
        for j in range(n):
            if omok_list[i][j] == "o":
                if cnt_o(omok_list, i, j) or diagonal_cnt(omok_list, i, j):
                    result = True
                    break            
        if result:
            break
    
    print(f"#{t} {res_dict[result]}")