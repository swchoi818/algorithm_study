import sys

input = sys.stdin.readline

def find_set(n):
    global p_dict
    if p_dict[n] != n:
        p_dict[n] = find_set(p_dict[n])
    return p_dict[n]

def union_set(a, b):
    global p_dict, rank, cnt_dict
    pa = find_set(a)
    pb = find_set(b)

    if pa != pb:
        if rank[pa] < rank[pb]:
            p_dict[pa] = pb
            cnt_dict[pb] += cnt_dict[pa]
        elif rank[pa] > rank[pb]:
            p_dict[pb] = pa
            cnt_dict[pa] += cnt_dict[pb]
        else:
            p_dict[pb] = pa
            rank[pb] += 1
            cnt_dict[pa] += cnt_dict[pb]

T = int(input())
for _ in range(T):
    F = int(input())

    p_dict = {}
    cnt_dict = {}
    rank = {}

    for _ in range(F):
        p1, p2 = input().split()
        if not p_dict.get(p1):
            p_dict[p1] = p1
            cnt_dict[p1] = 1
            rank[p1] = 1
        if not p_dict.get(p2):
            p_dict[p2] = p2
            cnt_dict[p2] = 1
            rank[p2] = 1
        union_set(p1, p2)
        print(cnt_dict[find_set(p1)])


