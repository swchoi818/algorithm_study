T = int(input())

for t in range(1, T + 1):
    cnt = 0
    A, B = map(str, input().split())
    i = 0
    while i < (len(A) - len(B) + 1):
        if A[i:i + len(B)] == B:
            cnt += 1
            i += len(B)
        else:
            i += 1
    print(f"#{t} {len(A) - (len(B) * cnt) + cnt}")