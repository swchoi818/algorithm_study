import sys

input = sys.stdin.readline
N, M = map(int, input().split())
num_list = [0] + list(map(int, input().split()))
idx_list = [tuple(map(int, input().split())) for _ in range(M)]
for i in range(1, N + 1):
    num_list[i] += num_list[i - 1]
print(*list(map(lambda x: num_list[x[1]] - num_list[x[0] - 1], idx_list)), sep='\n')
