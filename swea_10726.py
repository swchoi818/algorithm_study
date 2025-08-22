T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    tmp = 0
    for i in range(N):
        tmp += 2**i

    if M & tmp == tmp:
        print(f'#{t} ON')
    else:
        print(f'#{t} OFF')
