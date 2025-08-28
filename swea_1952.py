T = int(input())

for t in range(1, T + 1):
    day, month, month3, year = map(int, input().split())
    use_plan = [0] + list(map(int, input().split()))
    for i in range(1, 13):
        use_plan[i] = min(month, use_plan[i] * day)
        use_plan[i] += use_plan[i-1]
        if i < 3:
            continue
        use_plan[i] = min(use_plan[i], month3 + use_plan[i-3])

    print(f"#{t} {min(use_plan[12], year)}")