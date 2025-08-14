N = int(input())
K = int(input())

x = 0
y = -1
result = [[0 for _ in range(N)] for _ in range(N)]
dir = ((1, 0),(0, 1),(-1, 0),(0, -1))
num = N**2
di = 0
cnt = 1
length = N
locateK = ''
while length != 0:    
    for _ in range(length):
        x += dir[di][1]
        y += dir[di][0]
        result[y][x] = num
        if num == K:
            locateK = f"{y + 1} {x + 1}"
        num -= 1
    if di < 3:
        di += 1
    else : 
        di = 0
    cnt += 1    
    if cnt == 2:
        length -= 1
        cnt = 0
for i in result:
    print(' '.join(map(str, i)))
print(locateK)



