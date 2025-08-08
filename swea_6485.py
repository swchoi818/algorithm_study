T = int(input())
 
for test_case in range(1, T + 1):
    N = int(input())
    bus_route_list = [tuple(map(int,input().split())) for _ in range(N)]
    P = int(input())
    bus_stop_list = [int(input()) for _ in range(P)]
    bus_stop_cnt = {x : 0 for x in bus_stop_list}
    for i in bus_route_list:
        for j in range(i[0], i[1] + 1):
            if bus_stop_cnt.get(j) != None:
                bus_stop_cnt[j] += 1    
    print(f"#{test_case}", *[bus_stop_cnt[x] for x in bus_stop_list], sep=' ')