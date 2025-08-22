T = int(input())

for t in range(1, T + 1):
    N, hex_str = input().split()
    result = bin(int(hex_str, 16))
    n = (int(N) * 4) - len(result[2:])
    print(f"#{t} {'0'*n}{result[2:]}")
