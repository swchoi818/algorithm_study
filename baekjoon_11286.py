import heapq
import sys

input = sys.stdin.readline

N = int(input())
hq = []
result = []

for _ in range(N):
    cmd = int(input())
    if cmd != 0:
        heapq.heappush(hq, (abs(cmd), cmd))
    else:
        if hq:
            _, value = heapq.heappop(hq)
            result.append(value)
        else:
            result.append(0)

print(*result, sep='\n')