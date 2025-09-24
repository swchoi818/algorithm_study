def find_set(x):
    global people_list
    if x == people_list[x]:
        return x
    return find_set(people_list[x])


def union_set(x, y):
    px = find_set(x)
    py = find_set(y)

    people_list[px] = py


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    people_list = list(range(N + 1))
    for _ in range(M):
        a, b = map(int, input().split())
        union_set(a, b)
    result = 0
    for i in range(1, N + 1):
        if people_list[i] == i:
            result += 1

    print(f'#{t}', result)
