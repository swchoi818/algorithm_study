import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N = int(input())
M = int(input())

network_dict = defaultdict(list)
for _ in range(M):
    fr, to = map(int, input().split())
    network_dict[fr].append(to)
    network_dict[to].append(fr)

visited = set()
visited.add(1)
dq = deque()
dq.append(1)
cnt = 0
while dq:
    infection = dq.popleft()
    for node in network_dict[infection]:
        if node in visited:
            continue
        visited.add(node)
        dq.append(node)

print(len(visited) - 1)