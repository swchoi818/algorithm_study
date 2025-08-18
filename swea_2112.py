# dfs
# check_pass 합격 기준 리턴 True/ False
# dfs로 순차 탐색 통과하는 경우 나오면 현재 cnt를 result에 저장
# cnt가 result보다 커지면 안됨
# result = 0 이 아닐 때만 크기 비교

def check_pass():
    global film_mtr, D, W, K

    for i in range(W):
        cnt = 1
        for j in range(1, D):
            if film_mtr[j - 1][i] == film_mtr[j][i]:
                cnt += 1
            else:
                if cnt >= K:
                    continue
                cnt = 1
        if cnt < K:
            return False
        
    return True

def use_chemical(selected, cnt):
    global film_mtr, result, D, W
    if check_pass():
        if result == 0:
            result = cnt
            return
        result = min(result, cnt)
        return
    
    if cnt >= result and result != 0:
        return
    
    for i in range(selected, D):
        for ab in (0, 1):
            tmp = film_mtr[i].copy()
            film_mtr[i] = [ab] * W
            use_chemical(i + 1, cnt + 1)
            film_mtr[i] = tmp

T = int(input())

for t in range(1, T + 1):
    D, W, K = map(int, input().split())
    film_mtr = [list(map(int, input().split())) for _ in range(D)]
    result = 0

    use_chemical(0, 0)

    print(f"#{t} {result}")
