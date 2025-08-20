from collections import deque

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    pizza_list = list(map(int, input().split()))
    in_fire = [False] * M
    fire_pot = deque()
    idx = 0
    is_full = False
    result = 0
    while True:
        if len(fire_pot) == N:
            is_full = True
        if not is_full and idx < M:
            fire_pot.appendleft(idx)
            in_fire[idx] = True
            idx += 1
        else:
            fire_pot.rotate()
            if in_fire[fire_pot[0]]:
                pizza_list[fire_pot[0]] //= 2
                if pizza_list[fire_pot[0]] == 0:
                    fire_pot.popleft()
                    is_full = False
                    if len(fire_pot) == 1:
                        result = fire_pot.pop()
                        break
    print(f"#{t} {result + 1}")
