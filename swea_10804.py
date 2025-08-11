

def mirror_char(char):
    if char == 'b':
        return 'd'
    elif char == 'd':
        return 'b'
    elif char == 'p':
        return 'q'
    elif char == 'q':
        return 'p'


T = int(input())

for t in range(1, T+1):
    result = []
    str_list = list(input())
    while len(str_list) != 0:
        result.append(mirror_char(str_list.pop()))

    print(f"#{t} {''.join(result)}")
