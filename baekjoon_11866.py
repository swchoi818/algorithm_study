import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

cir_num = deque()

for i in range(1, N+1):
    cir_num.append(i)
result = []
while len(cir_num) != 0 :
    for _ in range(1, K):
        cir_num.append(cir_num.popleft())
    result.append(cir_num.popleft())

print(f"<{', '.join(map(str,result))}>")
