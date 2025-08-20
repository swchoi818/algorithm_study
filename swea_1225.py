from collections import deque

for t in range(1, 11):
    input()
    num_dq = deque(map(int, input().split()))
    is_end = False
    while True:
        for i in range(1, 6):
            num_dq[0] -= i
            num_dq.rotate(-1)
            if num_dq[7] <= 0:
                num_dq[7] = 0
                is_end = True
                break
        if is_end:
            break
    print(f"#{t} {' '.join(list(map(str, num_dq)))}")
