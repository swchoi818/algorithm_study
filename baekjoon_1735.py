import sys

input = sys.stdin.readline

def value_Euclid(a, b):
    a %= b
    if a == 0:
        return b
    return value_Euclid(b, a)

numerator_1, denominator_1 = map(int, input().split())
numerator_2, denominator_2 = map(int, input().split())

result_numerator = (numerator_1 * denominator_2) + (numerator_2 * denominator_1)
result_denominator = denominator_2 * denominator_1

gcd = value_Euclid(result_denominator, result_numerator)

result_numerator //= gcd
result_denominator //= gcd

print(result_numerator, result_denominator,sep=' ')

