N = int(input())

for _ in range(N):
    word = list(input())
    result = ''
    l = len(word)
    for _ in range(l):
        result += word.pop()
    print(result)