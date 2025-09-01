import sys


def operater(calc_list):
    i = 2
    res = int(calc_list[0])
    while i < len(calc_list):
        tmp = int(calc_list[i])
        if calc_list[i - 1] == '+':
            res += tmp
        elif calc_list[i - 1] == '-':
            res -= tmp
        elif calc_list[i - 1] == '*':
            res *= tmp
        i += 2
    return res


def dfs(idx):
    global calculate_list, visited, result
    tmp_list = []
    op = 0
    while op < N:
        if visited[op]:
            tmp_list.append(str(operater(calculate_list[op:op + 3])))
            op += 3
            continue
        tmp_list.append(calculate_list[op])
        op += 1

    result.append(operater(tmp_list))
    if idx >= N:
        return
    for i in range(idx, N - 2, 2):
        visited[i] = True
        dfs(i + 4)
        visited[i] = False


input = sys.stdin.readline

N = int(input())

calculate_list = list(input().rstrip())

result = []

visited = [False] * N

dfs(0)

print(max(result))
