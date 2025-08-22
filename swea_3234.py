import math


def scale_cnt(weight):
    global result, diff

    if diff > sum(weight):
        result += 2**len(weight) * math.factorial(len(weight))
        return
    if len(weight) == 0:
        result += 1
        return
    for i in range(len(weight)):
        diff += weight[i]
        scale_cnt(weight[:i] + weight[i + 1:])
        diff -= weight[i]
        if diff >= weight[i]:
            diff -= weight[i]
            scale_cnt(weight[:i] + weight[i + 1:])
            diff += weight[i]


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    weight_list = list(map(int, input().split()))
    diff = 0
    result = 0
    scale_cnt(weight_list)
    print(f'#{t}', result)