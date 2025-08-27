import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue_list = deque()

for i in range(N):
    cmd = input().rstrip()
    if cmd[0] == '1':
        queue_list.appendleft(int(cmd[2:]))
    elif cmd[0] == '2':
        queue_list.append(int(cmd[2:]))
    elif cmd[0] == '3':
        if len(queue_list) == 0:
            print(-1)
            continue
        print(queue_list.popleft())
    elif cmd[0] == '4':
        if len(queue_list) == 0:
            print(-1)
            continue
        print(queue_list.pop())
    elif cmd == '5':
        print(len(queue_list))
    elif cmd == '6':
        if len(queue_list) == 0:
            print(1)
            continue
        print(0)
    elif cmd == '7':
        if len(queue_list) == 0:
            print(-1)
            continue
        print(queue_list[0])
    elif cmd == '8':
        if len(queue_list) == 0:
            print(-1)
            continue
        print(queue_list[len(queue_list) -1])