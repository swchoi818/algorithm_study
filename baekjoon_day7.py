# n = int(input())
# cnt = 0
# while n != 0:
#     if n%3 == 0 and n < 15:
#         cnt += (n//3)
#         break
#     if n >= 5:
#         n -= 5
#         cnt += 1
#         if n == 0:
#             break
#     else:
#         cnt = -1
#         break
# print(cnt)

S = input()
str_set = set()
for i in range(len(S)):
    for j in range(i,len(S)):
        str_set.add(S[i:j+1])
print(len(str_set))