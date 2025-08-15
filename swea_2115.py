max_result = 0


def max_honey(beehv, idx, c, tmp):
    global max_result
    max_result = max(tmp, max_result)
    if (idx == len(beehv)):
        return
    if beehv[idx] > c:
        return
    
    for i in range(idx, len(beehv)):
        tmp += beehv[i] ** 2
        if beehv[i] <= c:
            max_honey(beehv, i + 1, c - beehv[i], tmp)
        tmp -= beehv[i] ** 2
        

T = int(input())

for t in range(1, T + 1):
    N, M, C = map(int, input().split())

    beehive_list = [list(map(int, input().split())) for _ in range(N)]
    result = []
    tmp_list = []
    for i in range(N):
        for j in range(N - M + 1):
            max_honey(beehive_list[i][j:j + M], 0, C, 0)
            tmp_list.append(max_result)
            max_result = 0
        result.append(tmp_list)
        tmp_list = []
    result2 = []
    for i in result:
        max_idx = 0
        max_idx2 = -1
        for j in range(len(i)):
            if i[j] > i[max_idx]:
                if j - max_idx >= M:
                    max_idx2, max_idx = max_idx, j
                else:
                    max_idx = j
        result2.append(i[max_idx])
        if max_idx2 != -1:
            result2.append(i[max_idx2])
    result2.sort(reverse=True)

    print(f"#{t} {result2[0] + result2[1]}")