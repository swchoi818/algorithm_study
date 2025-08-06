T = int(input())

def set_rect(r):
    rect = set()
    for i in range(r[0], r[2] + 1):
        for j in range(r[1], r[3] + 1):
            rect.add((i,j))
    return rect

for test_case in range(1, T + 1):
    N = int(input())
    rect1, rect2 = set()
    for _ in range(N):
        r = list(map(int, input().split()))
        if r[4] == 1:
            rect1 = rect1.union(set_rect(r))
        elif r[4] == 2:
            rect2 = rect2.union(set_rect(r))
    
    print(f"#{test_case}", len(rect1 & rect2))