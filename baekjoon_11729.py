result = []

def hanoi(n, start = 1, support = 2, end = 3):
    if n == 1:
        result.append(f"{start} {end}")
        return
    hanoi(n - 1, start, end, support)
    result.append(f"{start} {end}")
    hanoi(n - 1, support, start, end)

N = int(input())

hanoi(N)

print(len(result), *result, sep='\n')
