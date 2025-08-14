T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    player_list = sorted(list(map(int, input().split())))
    max_p = 0
    for i in range(N):
        for j in range(N - 1, i - 1, -1):
            diff = player_list[j] - player_list[i]
            if diff <= K:
                max_p = max(max_p, j - i + 1)
                break
    
    print(f"#{t} {max_p}")
            