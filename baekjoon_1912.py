import sys

input = sys.stdin.readline

n = int(input())

num_list = [0] + list(map(int, input().split()))

result = num_list[1]
tmp = 0
for i in range(1, n + 1):
    tmp += num_list[i]
    result = max(result, tmp)
    if  tmp < 0:
        tmp = 0

print(result)