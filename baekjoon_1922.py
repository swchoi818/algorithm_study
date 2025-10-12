def find_set(x):
    global p_list
    if p_list[x] != x:
        p_list[x] = find_set(p_list[x])
    return p_list[x]


def union_set(x, y, w):
    global rank, p_list, weight, cnt
    x = find_set(x)
    y = find_set(y)

    if x != y:
        weight += w
        cnt += 1
        if rank[x] > rank[y]:
            p_list[y] = x
        elif rank[x] < rank[y]:
            p_list[x] = y
        else:
            p_list[y] = x
            rank[x] += 1


N = int(input())
M = int(input())
p_list = list(range(N + 1))
cnt = 0
weight = 0
rank = [0] * (N + 1)
graph_info = [list(map(int, input().split())) for _ in range(M)]
graph_info.sort(key=lambda x: x[2])
for i in range(M):
    n1, n2, w = graph_info[i]
    union_set(n1, n2, w)
    if cnt == N:
        break

print(weight)
