from decimal import Decimal, getcontext


def part_average(selected, remain):
    global result
    if len(selected) != 0:
        result += sum(selected) / (len(selected))
    for i in range(len(remain)):
        selected.append(remain[i])
        part_average(selected, remain[i + 1:])
        selected.remove(remain[i])


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    result = 0
    part_average([], num_list[:])
    d = Decimal(str(result / (2 ** N - 1)))
    print(f"#{t}", d.quantize(Decimal('1e-20')).normalize())
