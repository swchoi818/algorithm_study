import sys

def prefix_sum(n, arr):
    prefixSum = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1] + arr[i-1][j-1]
    return prefixSum

input = sys.stdin.readline

N, M = map(int, input().split())

arr_n = [list(map(int, input().split())) for _ in range(1, N + 1)]

prefix_arr = prefix_sum(N, arr_n)
xy = [list(map(int, input().split())) for _ in range(M)]


for m in xy:
    result = 0
    i, j, x, y = m[0], m[1], m[2], m[3]
    result = prefix_arr[x][y] - prefix_arr[i-1][y] - prefix_arr[x][j-1] + prefix_arr[i-1][j-1]
    print(result)
