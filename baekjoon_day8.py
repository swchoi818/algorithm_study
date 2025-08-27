import sys

input = sys.stdin.readline


def value_Euclid(a, b):
    a %= b
    if a == 0:
        return b
    return value_Euclid(b, a)


T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    if a < b:
        a, b = b, a
    print((a * b) // value_Euclid(a, b))
