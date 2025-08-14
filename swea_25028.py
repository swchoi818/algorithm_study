T = int(input())

for t in range(1, T + 1):
    N = int(input())
    subject_list = []
    for _ in range(N):
        i = input()
        if i == '0':
            subject_list.append([i])
        else:
            subject_list.append(list(map(int, i.split())))
    comp_set = set()
    result = 0
    while True:
        tmp_list = []
        for i in range(N):
            if subject_list[i][0] != '0':
                cnt = subject_list[i][0]
                tmp2 = []
                for j in range(1, cnt + 1):
                    tmp2.append(subject_list[i][j])
                if not (set(tmp2) - comp_set):
                    tmp_list.append(i + 1)
            else:
                tmp_list.append(i + 1)

        if not (set(tmp_list) - comp_set):
            result = -1
            break
        comp_set = comp_set.union(set(tmp_list))
        result += 1
        if len(comp_set) == N:
            break
    print(f"#{t} {result}")