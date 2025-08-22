T = int(input())


def change_digit(change_cnt):
    global result
    if change_cnt == cnt:
        result = max(result, int("".join(num)))
        return
    current_state = (change_cnt, "".join(num))
    if current_state in visited:
        return
    visited.add(current_state)

    for i in range(len(num) - 1):
        for j in range(i + 1, len(num)):
            num[i], num[j] = num[j], num[i]
            change_digit(change_cnt + 1)
            num[i], num[j] = num[j], num[i]


for t in range(1, T + 1):
    num, cnt = map(int, input().split())
    result = 0
    change_cnt = 0
    visited = set()
    num = list(str(num))
    change_digit(0)
    print(f"#{t}", result)
