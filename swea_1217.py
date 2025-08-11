def square(n, m):
    if m == 0:
        return 1
    return n * square(n, m-1)

for _ in range(1, 11):
    tc = int(input())
    N, M = map(int, input().split())
    print(f"#{tc}", square(N,M))