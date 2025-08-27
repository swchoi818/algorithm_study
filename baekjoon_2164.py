from collections import deque

import sys

input = sys.stdin.readline

N = int(input())

card = deque()
if N == 1:
    print(1)
    exit()

for i  in range(2,N+1,2):
    card.append(i)
if N%2 == 1:
    card.append(card.popleft())
while len(card) != 1:
    card.popleft()
    card.append(card.popleft())

print(card.pop())
