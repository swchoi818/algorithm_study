def min_sum(depth):
    global result, tmp, visited
    if result != 0 and tmp >= result:
        return
    if depth == N:
        if result != 0:
            result = min(tmp, result)
        else:
            result = tmp
        return
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        tmp += num_list[depth][i]
        min_sum(depth + 1)
        tmp -= num_list[depth][i]
        visited[i] = False


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    tmp = 0
    visited = [False] * N
    min_sum(0)
    print(f"#{t} {result}")
