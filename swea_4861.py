T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    str_mtr = [input() for _ in range(N)]
    str_mtr_turn = list(zip(*str_mtr))
    result = ''
    for i in range(N):
        for j in range(N - M + 1):
            temp1 = str_mtr[i][j:j + M]
            temp2 = ''.join(str_mtr_turn[i][j:j + M])
            if temp1 == temp1[::-1]:
                result = temp1
                break
            if temp2 == temp2[::-1]:
                result = temp2
                break
        if result != '':
            break
    print(f"#{test_case}", result)