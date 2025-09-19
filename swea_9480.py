def dfs(idx, selected):
    global result, word_list
    if len(selected) == 26:
        result += 2 ** (N - idx)
        return
    for i in range(idx, N):
        dfs(i + 1, selected.union(set(word_list[i])))


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    word_list = [list(input().strip()) for _ in range(N)]
    result = 0
    dfs(0, set())
    print(f'#{t}', result)
