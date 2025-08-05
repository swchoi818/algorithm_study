T = 10

for test_case in range(1, T + 1):
    N = int(input())
    cnt = 0
    dir = [-2, -1, 1, 2]
    building_list = list(map(int, input().split()))
    
    for i in range(2, N - 2):
        next_building = []
        for j in dir:
            next_building.append(building_list[i + j])
        next_max = max(next_building)
        if next_max < building_list[i]:
            cnt += (building_list[i] - next_max)
    print(f"#{test_case}", cnt)