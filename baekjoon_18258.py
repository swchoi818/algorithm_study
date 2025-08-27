import sys
from queue import Queue
from collections import deque
input = sys.stdin.readline

N = int(input())
queue_list = deque()

for i in range(N):
    cmd = input().rstrip()
    if cmd[:4] == 'push':
        queue_list.append(int(cmd[5:]))
    elif cmd[:3] == 'pop':
        if len(queue_list) == 0:
            print(-1)
            continue
        print(queue_list.popleft())
    elif cmd == 'size':
        print(len(queue_list))
    elif cmd == 'empty':
        if len(queue_list) == 0:
            print(1)
            continue
        print(0)
    elif cmd == 'front':
        if len(queue_list) == 0:
            print(-1)
            continue
        print(queue_list[0])
    elif cmd == 'back':
        if len(queue_list) == 0:
            print(-1)
            continue
        print(queue_list[len(queue_list) -1])

    