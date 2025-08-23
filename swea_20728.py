T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    candy_cnt = sorted(list(map(int, input().split())))
    result = []
    for i in range(N - K + 1):
        result.append(candy_cnt[i + K - 1] - candy_cnt[i])

    print(f"#{t}", min(result))
