T = int(input())

for t in range(1, T + 1):
    word = input().strip()
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - 1 - i]:
            print(f'#{t}', 0)
            break
    else:
        print(f'#{t}', 1)
