def permutation(remain, score):
    global result
    if len(remain) == 1:
        result = max(result, score + remain.pop())
        return

    for i in range(len(remain)):
        if i == 0:
            permutation(remain[i + 1:], score + remain[i + 1])
        elif i == len(remain) - 1:
            permutation(remain[:i], score + remain[i - 1])
        else:
            permutation(remain[:i] + remain[i + 1:], score + remain[i - 1] * remain[i + 1])

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    score_list = list(map(int, input().split()))
    result = 0
    permutation(score_list.copy(), 0)

    print(f"#{t}", result)
