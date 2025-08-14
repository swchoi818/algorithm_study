T = int(input())

for t in range(1, T + 1):
    N = int(input())
    state1 = int('0b' + input().replace(" ", ""), 2)
    state2 = int('0b' + input().replace(" ", ""), 2)
    state3 = bin(state1 ^ state2)
    tmp = ''
    cnt = 0
    for i in state3[2:]:
        if i != tmp:
            cnt += 1
            tmp = i

    print(f"#{t} {cnt}")