# 집합으로 만들어서 discard

for t in range(1, 11):
    V, E = map(int, input().split())

    e_list = list(map(int, input().split()))
    work_list = [None] + [set() for _ in range(V)]
    for i in range(1, len(e_list), 2):
        work_list[e_list[i]].add(e_list[i - 1])
    result = []
    is_end = False
    while True:
        for i in range(1, V + 1):
            if not work_list[i]:
                result.append(i)
                work_list[i].add(-1)
                if len(result) == V:
                    is_end = True
                    break
                for j in range(1, V + 1):
                    work_list[j].discard(i)
        if is_end:
            break

    print(f"#{t}", *result, sep=" ")
