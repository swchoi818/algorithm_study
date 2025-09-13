N = int(input())

option_list = [input() for _ in range(N)]
shortcut_key = set(' ')

for i in option_list:
    tmp = i.split()
    for j in range(len(tmp)):
        if tmp[j][0].upper() not in shortcut_key and tmp[j][0].lower() not in shortcut_key:
            shortcut_key.add(tmp[j][0].upper())
            shortcut_key.add(tmp[j][0].lower())
            tmp[j] = tmp[j].replace(tmp[j][0],f"[{tmp[j][0]}]", 1)
            res = ' '.join(tmp)
            print(res)
            break
    else:
        for j in i:
            if j.upper() not in shortcut_key and j.lower() not in shortcut_key:
                shortcut_key.add(j.upper())
                shortcut_key.add(j.lower())
                res = i.replace(j, f'[{j}]', 1)
                print(res)
                break
        else:
            print(i)
