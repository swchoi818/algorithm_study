import sys

# n, m = map(int, sys.stdin.readline().split())

# card = list(map(int,sys.stdin.readline().split()))

# result = 0
# for i in range(n - 2):
#     for j in range(i + 1,n):
#         for k in range(j + 1,n):
#             sum = card[i] + card[j] + card[k]
#             if sum <= m:
#                result = max(result,sum)
#                if result == m:
#                    break

# print(result)

n =int(sys.stdin.readline())

a = 0
result = 0
for i in range(1, n):
    digit = str(i).strip()
    for j in digit:
        a += int(j)
    a += i
    if n == a:
        result = i
        break
    a = 0

print(result)
    