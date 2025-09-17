N = int(input())

cost_painting = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(3):
        cost_painting[i][j] += min(cost_painting[i-1][:j] + cost_painting[i-1][j+1:])

print(min(cost_painting[-1]))
