from collections import deque

for t in range(1, 11):
    N, start = map(int, input().split())
    connect_list = list(map(int, input().split()))
    graph_dict = {}
    for i in range(0, N, 2):
        if graph_dict.get(connect_list[i]):
            graph_dict[connect_list[i]].add(connect_list[i + 1])
        else:
            graph_dict[connect_list[i]] = {connect_list[i + 1]}
    dq = deque()
    dq.append((start, 0))
    visited = set()
    result = 0
    last_contact = 0
    while dq:
        node, dist = dq.popleft()
        if last_contact < dist or (dist == last_contact and result < node):
            last_contact = dist
            result = node

        if not graph_dict.get(node):
            continue
        for i in list(graph_dict[node]):
            if i not in visited:
                visited.add(i)
                dq.append((i, dist + 1))

    print(f'#{t}', result)
