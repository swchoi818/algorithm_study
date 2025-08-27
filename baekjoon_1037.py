import sys

N = int(input())

factor_list = sorted(list(map(int,input().split())))

print(factor_list[0] * factor_list[len(factor_list) - 1])
