from collections import deque
T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    fee_list = [int(input()) for _ in range(N)]
    weight_list = [int(input()) for _ in range(M)]
    seq_list = [abs(int(input())) for _ in range(M * 2)]
    is_fill = [False] * N
    is_enter = [False] * M
    car_locate = [0] * M
    result = 0
    wait_car = deque()
    for c in seq_list:
        if is_enter[c - 1]:
            idx = car_locate[c-1]
            is_fill[idx] = False
            if wait_car:
                wc = wait_car.popleft()
                result += (fee_list[idx] * weight_list[wc - 1])
                print(result)
                is_fill[idx] = True
                is_enter[wc - 1] = True
                car_locate[wc - 1] = idx
        else:
            for i in range(N):
                if not is_fill[i]:
                    result += (fee_list[i] * weight_list[c - 1])
                    print(result)
                    is_fill[i] = True
                    is_enter[c - 1] = True
                    car_locate[c - 1] = i
                    break
            else:
                wait_car.append(c)


    print(f"#{t} {result}")   
