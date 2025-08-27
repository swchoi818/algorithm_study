import sys

input = sys.stdin.readline

N = int(input())

meeting_time = []

for _ in range(N):
    meeting_time.append(tuple(map(int,input().split())))

meeting_time.sort(key=lambda x : (x[1], x[0]))


end = meeting_time[0][1]
cnt = 1
for i in range(1, N):
    if end <= meeting_time[i][0]:
        end = meeting_time[i][1]
        cnt += 1

print(cnt)