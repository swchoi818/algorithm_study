import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
cir_num = deque(map(int, input().split()))
result = []
index_list = deque(map(int, range(1,len(cir_num)+1)))
move = cir_num.popleft()
result.append(index_list.popleft())
while len(cir_num) != 0:  
    if move > 0:
        for _ in range(abs(move)-1):
            cir_num.append(cir_num.popleft())
            index_list.append(index_list.popleft())
        move = cir_num.popleft()
        result.append(index_list.popleft())
    else:
        for _ in range(abs(move)-1):
            cir_num.appendleft(cir_num.pop())
            index_list.appendleft(index_list.pop())
        move = cir_num.pop()
        result.append(index_list.pop())
        
print(' '.join((map(str,result))))
