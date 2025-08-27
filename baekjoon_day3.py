# def MenOfPassion(A, n):
#     sum = 0
#     for i in range(1, n):
#         sum += A[i] # 코드1
#     return sum
# n = int(input())
# print(n,"\n1")

# n = int(input())
# print(n**2,"\n2")

# n = int(input())
# # print(int(n*(n-1)/2),"\n2")
# # def MenOfPassion(n) :
# #     count = 0
# #     for i in range(1, n - 2):
# #         for j in range(i + 1, n - 1):
# #             for k in range(j + 1, n):
# #                 count += 1; # 코드1
# #     return count

# # print(MenOfPassion(int(input())),"\n3")

# print((n-2)*(n-1) *n//6,"\n3")
import sys

a = sys.stdin.readline()
c = int(sys.stdin.readline())
n0 = int(sys.stdin.readline())

a1, a0 = map(int,a.split())

if c > a1 and (a1 * n0 + a0 <= c * n0):
    print(1)
elif c == a1 and a0 <= 0:
    print(1)
else:
    print(0)