T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    weight = list(reversed(sorted(map(int, input().split()))))
    truck = list(reversed(sorted(map(int, input().split()))))
    result = 0
    i, j = 0, 0
    while True:
        try:
            if truck[j] < weight[i]:
                i += 1
                continue
            result += weight[i]
            j += 1
            i += 1
        except IndexError:
            break

    print(f"#{t}",result)
