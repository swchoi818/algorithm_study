T = int(input())

N = 0
X = 0

def cnt_line(height_mtr):
    last_h = 0
    result = 0
    for i in range(N):        
        cnt = 1
        last_h = 0
        is_low = False
        for j in range(N):
            if height_mtr[i][j] == last_h:
                cnt += 1
                continue
            if last_h == 0:
                last_h = height_mtr[i][j]
                continue
            if is_low and cnt < X:
                break
            elif is_low:
                is_low = False
                cnt -= X
            if height_mtr[i][j] - last_h == 1:
                if cnt < X:
                    break
                cnt = 1
            elif height_mtr[i][j] - last_h == -1:
                is_low = True
                cnt = 1
            else:
                break
            last_h = height_mtr[i][j]
        else:
            if is_low and cnt >= X:
                result += 1
            elif not is_low:
                result += 1
    return result

for t in range(1, T + 1):
    N, X = map(int, input().split())

    height_mtr = [list(map(int, input().split())) for _ in range(N)]
    height_mtr2 = list(zip(*height_mtr))
    result = cnt_line(height_mtr)
    result += cnt_line(height_mtr2)

    print(f"#{t} {result}")