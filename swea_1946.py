T = int(input())

for t in range(1, T + 1):
    N = int(input())
    result = ''
    for i in range(N):
        eng_str, cnt = input().split()
        result += eng_str * int(cnt)
    print(f"#{t}")
    for i in range(len(result)):
        if i%10 == 0 and i != 0:
            print()
        print(result[i], end='')
    print()