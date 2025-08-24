def calculate(oper_l):
    result = num_list[0]
    for i in range(N - 1):
        if oper_l[i] == '+':
            result += num_list[i + 1]
        elif oper_l[i] == '-':
            result -= num_list[i + 1]
        elif oper_l[i] == '*':
            result *= num_list[i + 1]
        elif oper_l[i] == '/':
            result = int(result / num_list[i + 1])

    return result


def make_oper_comb(selected, remain):
    global res_oper, visited
    if len(remain) == 0:
        if tuple(selected) in visited:
            return
        visited.add(tuple(selected))
        res_oper.append(calculate(selected))
        return
    for i in range(len(remain)):
        selected.append(remain[i])
        make_oper_comb(selected, remain[:i] + remain[i + 1:])
        selected.pop()


op = ['+', '-', '*', '/']

N = int(input())
visited = set()
num_list = list(map(int, input().split()))
oper_tmp = list(map(int, input().split()))
oper_list = []
res_oper = []
for i in range(4):
    oper_list.extend(op[i] * oper_tmp[i])

make_oper_comb([], oper_list[:])

print(max(res_oper))
print(min(res_oper))
