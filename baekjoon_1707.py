from collections import defaultdict, deque
import sys

input = sys.stdin.readline

K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(E):
        v, c = map(int, input().split())
        graph[v].append(c)
        graph[c].append(v)
    group = [0] * (V + 1)
    is_bipartite = 'YES'
    for i in range(1, V + 1):
        if group[i]:
            continue
        group[i] = 1
        dq = deque([i])
        while dq:
            v = dq.popleft()
            for c in graph[v]:
                if not group[c]:
                    group[c] = 3 - group[v]
                    dq.append(c)
                elif group[c] == group[v]:
                    is_bipartite = 'NO'
                    break
            if is_bipartite == 'NO':
                break
        if is_bipartite == 'NO':
            break

    print(is_bipartite)