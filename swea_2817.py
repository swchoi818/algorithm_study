def part_sum(selected, remain):
    global result
    if selected > K:
        return
    if selected == K:
        result += 1
        return
    for i in range(len(remain)):
        selected += remain[i]
        part_sum(selected, remain[i + 1:])
        selected -= remain[i]


T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    num_list = list(map(int, input().split()))
    result = 0
    part_sum(0, num_list[:])
    print(f"#{t}", result)
