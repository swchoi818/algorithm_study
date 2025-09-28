def multiple(a, b):
    if a == 1:
        return 1
    if b == 1:
        return a % C
    if b == 0:
        return 1
    divide = multiple(a, b // 2)
    if b % 2 == 0:
        return (divide * divide) % C
    else:
        return (divide * divide * a) % C
A, B, C = map(int, input().split())

print(multiple(A, B))