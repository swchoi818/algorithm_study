dir_4 = [(1, 0), (-1, 0), (0, -1), (0, 1)]

class Atomic:
    def __init__(self, x, y, direct, energy):
        self.x = x
        self.y = y
        self.energy = energy
        self.direct = dir_4[direct]

    def move(self):
        self.y += self.direct[0]
        self.x += self.direct[1]
        return self.x, self.y

    def get_location(self):
        return self.x, self.y


def crash_atomic(a1, a2):
    global result, atomic
    result += atomic[a2].energy
    atomic[a2].energy = 0
    result += atomic[a1].energy
    atomic[a1].energy = 0

T = int(input())
for t in range(1, T + 1):
    result = 0
    N = int(input())
    atomic = [Atomic(*list(map(int, input().split()))) for _ in range(N)]
    locate_dict = {}
    for i in range(N):
        locate_dict[atomic[i].get_location()] = i

    while True:
        is_end = True
        moved = {}
        for i in range(N):
            if locate_dict.get(atomic[i].get_location()) is None:
                continue
            if atomic[i].energy == 0:
                locate_dict.pop(atomic[i].get_location())
                continue
            x, y = atomic[i].get_location()
            if -1000 <= x <= 1000 and -1000 <= y <= 1000:
                is_end = False
                ay, ax = atomic[i].direct
                if locate_dict.get((x + ax, y + ay)) is not None:
                    if atomic[locate_dict[(x + ax, y + ay)]].direct == (-ay, -ax):
                        crash_atomic(i, locate_dict.pop((x + ax, y + ay)))
                        locate_dict.pop((x, y))
                        continue
                nx, ny = atomic[i].move()
                if moved.get((nx, ny)) is None:
                    moved[(nx, ny)] = locate_dict.pop((x, y))
                else:
                    crash_atomic(locate_dict.pop((x, y)), moved[(nx, ny)])
        locate_dict = moved.copy()
        if is_end:
            break

    print(f'#{t} {result}')
