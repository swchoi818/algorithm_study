T = int(input())

for t in range(1, T + 1):
    N = float(input())
    result = ''
    while N != 0.0:
        result += str(int(N*2))
        N = (N*2)%1
        if len(result) >= 12:
            print(f"#{t} overflow")
            break
    else:
        print(f"#{t} {result}")
