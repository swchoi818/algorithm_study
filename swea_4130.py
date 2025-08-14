from collections import deque

T = int(input())

magnet_list = []


def turn_magnet(loc, direction, is_left, is_right):
    r_loc = loc + 1
    l_loc = loc - 1
    if is_right and 0 <= r_loc < 4 and magnet_list[loc][2] != magnet_list[r_loc][6]:
        turn_magnet(r_loc, direction * -1, False, True)
    if is_left and 0 <= l_loc < 4 and magnet_list[loc][6] != magnet_list[l_loc][2]:
        turn_magnet(l_loc, direction * -1, True, False)

    magnet_list[loc].rotate(direction)


for t in range(1, T + 1):
    K = int(input())
    magnet_list = [deque(list(map(int, input().split()))) for _ in range(4)]
    turn_info = [tuple(map(int, input().split())) for _ in range(K)]

    for i, j in turn_info:
        turn_magnet(i - 1, j, True, True)
    result = 0
    for i in range(len(magnet_list)):
        result += magnet_list[i][0] * (2 ** i)
    print(f"#{t} {result}")