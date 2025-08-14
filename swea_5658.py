from collections import deque

T = int(input())

for t in range(1, T + 1):
    hex_dict = {}
    N, K = map(int, input().split())
    password = deque(input())
    pwd_list = list(password)
    
    for _ in range(N//4):
        for i in range(4):
            st = i*N//4
            hex_key = ''.join(pwd_list[st:st + N//4])
            hex_dict[hex_key] = int(hex_key, 16)
        password.appendleft(password.pop())
        pwd_list = list(password)

    pwd_list = list(reversed(sorted(hex_dict.values())))
    print(f"#{t} {pwd_list[K - 1]}")