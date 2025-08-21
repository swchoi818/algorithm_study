def scale_cnt(scale, weight, sq_t):
    global result

    if sum(scale[:N]) > sum(scale[N:]):
        return
    if len(weight) == 0:
        result += 1
        return
    for i in range(len(weight)):
        scale[sq_t] = weight[i]
        scale_cnt(scale, weight[:i] + weight[i + 1:], sq_t + 1)
        scale[sq_t] = 0

        scale[sq_t + N] = weight[i]
        scale_cnt(scale, weight[:i] + weight[i + 1:], sq_t + 1)
        scale[sq_t + N] = 0


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    weight_list = list(map(int, input().split()))
    scale_l = [0] * N * 2
    result = 0
    scale_cnt(scale_l, weight_list, 0)
    print(f'#{t}', result)
