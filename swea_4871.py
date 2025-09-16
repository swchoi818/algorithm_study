from collections import deque

T = int(input())

for t in range(1, T + 1):
    V, E = map(int, input().split())
    graph_dict = {}
    visited = [False] * (V + 1)
    for _ in range(E):
        k, v = map(int, input().split())
        if graph_dict.get(k):
            graph_dict[k].append(v)
            continue
        graph_dict[k] = [v]
    start, end = map(int, input().split())
    dq = deque()
    dq.append(start)
    visited[start] = True
    result = 0
    while dq:
        now_v = dq.popleft()
        if now_v == end:
            result = 1
            break
        if not graph_dict.get(now_v):
            continue
        for i in graph_dict[now_v]:
            if visited[i]:
                continue
            dq.append(i)
            visited[i] = True

    print(f'#{t}', result)
