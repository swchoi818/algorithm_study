import heapq


def get_dist(start, end):
    x, y = start
    nx, ny = end

    return (abs(x - nx) ** 2) + (abs(y - ny) ** 2)


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    locate = []
    for i in range(N):
        locate.append((x_list[i], y_list[i]))
    E = float(input())
    visited = [False] * N
    queue = []
    result = 0
    heapq.heappush(queue, (0, 0))
    while queue:
        w, st = heapq.heappop(queue)
        if visited[st]:
            continue
        visited[st] = True
        result += w
        for i in range(len(locate)):
            heapq.heappush(queue, (get_dist(locate[st], locate[i]), i))

    print(f'#{t}', round(E * result))
