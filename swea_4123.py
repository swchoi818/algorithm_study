def make_oper_comb(idx, result):
    global res_oper
    if idx == N:
        res_oper.append(result)
        return
    result_tmp = 0
    for i in range(4):
        if oper_list[i] > 0:
            oper_list[i] -= 1
            if i == 0:
                result_tmp = result + num_list[idx]
            elif i == 1:
                result_tmp = result - num_list[idx]
            elif i == 2:
                result_tmp = result * num_list[idx]
            elif i == 3:
                result_tmp = int(result / num_list[idx])
            make_oper_comb(idx + 1, result_tmp)
            oper_list[i] += 1


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    oper_list = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    res_oper = []

    make_oper_comb(1, num_list[0])

    print(f"#{t}", max(res_oper) - min(res_oper))
