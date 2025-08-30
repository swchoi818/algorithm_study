def dfs(st_1, st_2, idx):
    global result, stair_len, people_list
    if idx == len(people_list):
        st_1.sort()
        st_2.sort()
        end_time_1 = []
        end_time_2 = []
        for i in range(len(st_1)):
            if i >= 3:
                end_time_1.append(max(end_time_1[i - 3], st_1[i] + 1) + stair_len[0])
            else:
                end_time_1.append(st_1[i] + stair_len[0] + 1)
        for i in range(len(st_2)):
            if i >= 3:
                end_time_2.append(max(end_time_2[i - 3], st_2[i] + 1) + stair_len[1])
            else:
                end_time_2.append(st_2[i] + stair_len[1] + 1)
        res = 0
        if len(end_time_1) != 0:
            res = end_time_1.pop()
        if len(end_time_2) != 0:
            res = max(res, end_time_2.pop())
        result.append(res)
        return
    st_1.append(people_dist[idx][0])
    dfs(st_1[:], st_2[:], idx + 1)
    st_1.pop()
    st_2.append(people_dist[idx][1])
    dfs(st_1[:], st_2[:], idx + 1)
    st_2.pop()


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    room_mtr = [list(map(int, input().split())) for _ in range(N)]
    people_list = []
    stair_list = []
    stair_len = []
    result = []
    stair1 = []
    stair2 = []
    for i in range(N):
        for j in range(N):
            if room_mtr[i][j] == 1:
                people_list.append((i, j))
            elif room_mtr[i][j] > 1:
                stair_list.append((i, j))
                stair_len.append(room_mtr[i][j])

    people_dist = []

    for py, px in people_list:
        tmp = []
        for sy, sx in stair_list:
            tmp.append(abs(py - sy) + abs(px - sx))
        people_dist.append(tmp)

    dfs(stair1, stair2, 0)

    print(f"#{t}", min(result))
