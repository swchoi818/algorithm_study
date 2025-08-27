import sys
from collections import Counter
input = sys.stdin.readline

N, M = map(int,input().split())

word_list = Counter()

for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        word_list[word] += 1
result = dict(sorted(word_list.items(), key=lambda x : (-x[1], -len(x[0]), x[0])))

print(*result.keys(),sep= '\n')

# 시간초과... lambda를 이용한 sorted 공부 필요

# import sys
# from collections import Counter
# input = sys.stdin.readline

# N, M = map(int,input().split())

# word_list = Counter()

# for _ in range(N):
#     word = input().rstrip()
#     if len(word) >= M:
#         word_list[word] += 1
# word_list = dict(sorted(word_list.items()))
# result = list(sorted(word_list.items(), key=lambda x : x[1], reverse=True))
# for i in range(1, len(result)):
#         a = i
#         for j in range(i-1, -1, -1):
#             if result[a][1] == result[j][1] and len(result[a][0]) > len(result[j][0]):
#                 result[a],result[j] = result[j],result[a]
#                 a = j
#             else:
#                 break
# result = dict(result)
# print(*result.keys(),sep= '\n')