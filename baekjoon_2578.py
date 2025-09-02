from collections import defaultdict, deque

N, T = map(int, input().split())
yx_set = set()

for _ in range(N):
    x, y = map(int, input().split())
    yx_set.add((x, y))

dq = deque()
dq.append((0, 0, 0))
result = -1

while dq and result == -1:
    a, b, dist = dq.popleft()

    for nx in range(a - 2, a + 3):
        for ny in range(b - 2, b + 3):
            if (nx, ny) in yx_set:
                if ny == T:
                    result = dist + 1
                    break
                dq.append((nx, ny, dist + 1))
                yx_set.discard((nx, ny))
    if result != -1:
        break

print(result)
