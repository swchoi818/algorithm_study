T = int(input())

for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    charge_list = list(map(int, input().split()))
    now_locate = 0
    next_charge = 0
    cnt = 0
    while True:
        for i in range(now_locate + 1, now_locate + K + 1):
            if i in charge_list:
                next_charge = i
        if now_locate < next_charge:
            now_locate = next_charge
            cnt += 1
        else:
            cnt = 0
            break
        if now_locate + K >= N:
            break
    print(f"#{test_case}",cnt)