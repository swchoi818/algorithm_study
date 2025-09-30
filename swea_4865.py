T = int(input())

for t in range(1, T + 1):
    pattern = {key: 0 for key in input().strip()}
    word = input().strip()

    for i in word:
        if pattern.get(i) != None:
            pattern[i] += 1

    print(f'#{t}', max(pattern.values()))
