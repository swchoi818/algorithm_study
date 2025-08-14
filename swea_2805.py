T = int(input())
for t in range(1, T + 1):
    N = int(input())
    mtr = [list(input()) for _ in range(N)]
    st_point = N//2
    ed_point = N//2
    move = -1
    result = 0
    for i in range(N):
        for j in range(st_point, ed_point + 1):
            result += int(mtr[i][j])
        st_point += move
        ed_point -= move
        if st_point == 0:
            move = 1
    
    print(f"#{t} {result}")
