def find_set(x):
    global p_list
    if p_list[x] != x:
        p_list[x] = find_set(p_list[x])
    return p_list[x]

def union_set(x, y, w):
    global rank, p_list, result, cnt_v
    x = find_set(x)
    y = find_set(y)

    if x != y:
        result += w
        cnt_v += 1
        if rank[x] > rank[y]:
            p_list[y] = x
        elif rank[x] < rank[y]:
            p_list[x] = y
        else:
            p_list[y] = x
            rank[x] += 1

V, E = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(E)]
p_list = list(range(V + 1))
rank = [0] * (V + 1)
graph.sort(key=lambda x: x[2])
result = 0
cnt_v = 0
for i in range(E):
        n1, n2, w = graph[i]
        union_set(n1, n2, w)
        if cnt_v == V:
            break

print(result)
