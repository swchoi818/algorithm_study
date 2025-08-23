T = int(input())

for t in range(1, T + 1):
    N = int(input())
    schedule_list = [tuple(map(int, input().split())) for _ in range(N)]
    schedule_list.sort(key=lambda x: (x[1], x[0]))

    end = schedule_list[0][1]
    cnt = 1
    for i in range(1, N):
        if end <= schedule_list[i][0]:
            end = schedule_list[i][1]
            cnt += 1

    print(f"#{t} {cnt}")
