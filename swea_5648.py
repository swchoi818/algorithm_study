dir_4 = [(1, 0), (-1, 0), (0, -1), (0, 1)]


class Atomic:
    def __init__(self, x, y, direct, energy):
        self.x = x * 2
        self.y = y * 2
        self.energy = energy
        self.direct = dir_4[direct]

    def move(self):
        self.y += self.direct[0]
        self.x += self.direct[1]
        return self.x, self.y

    def get_location(self):
        return self.x, self.y


def crash_atomic(atom):
    global result, atomic
    for a in atom:
        result += atomic[a].energy
        atomic[a].energy = 0


T = int(input())

for t in range(1, T + 1):
    result = 0
    N = int(input())
    atomic = [Atomic(*list(map(int, input().split()))) for _ in range(N)]

    while True:
        is_end = True
        locate_dict = {}
        for i in range(len(atomic)):
            if atomic[i].energy == 0:
                continue
            nx, ny = atomic[i].move()
            if -2000 <= nx <= 2000 and -2000 <= ny <= 2000:
                is_end = False
                if locate_dict.get((nx, ny)) is None:
                    locate_dict[(nx, ny)] = [i]
                else:
                    locate_dict[(nx, ny)].append(i)

        tmp = []
        for i in locate_dict:
            if len(locate_dict[i]) == 1:
                locate_dict[i] = locate_dict[i][0]
            else:
                crash_atomic(locate_dict[i])
                tmp.append(i)

        for i in tmp:
            locate_dict.pop(i)

        if is_end:
            break

    print(f'#{t} {result}')
