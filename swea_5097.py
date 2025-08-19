from collections import deque

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    num_list = deque(map(int, input().split()))

    for _ in range(M):
        num_list.rotate(-1)
    
    print(f"#{t}",num_list[0])
