def turnArray(array, size):
    result = [[0 for _ in range(size)] for _ in range(size)]
        
    for i in range(size):
        for j in range(size):
            result[i][j] = (array[size - j - 1][i])
    
    return result

T = int(input())
grid = [[] for _ in range(T)]
n = [0 for _ in range(T)]
for test_case in range(T):
    n[test_case] = int(input())
    grid[test_case] = [0 for _ in range(n[test_case])]
    for i in range(0, n[test_case]):
        grid[test_case][i] = list(map(int, input().split()))
    
for t in range(T):
    result = {'90': [[]], '180': [[]], '270': [[]]}
    result['90'] = turnArray(grid[t], n[t])
    result['180'] = turnArray(result['90'], n[t])
    result['270'] = turnArray(result['180'], n[t])
    print(f"#{t + 1}")
    for i in range(n[t]):
        print("".join(map(str, result['90'][i])), "".join(map(str, result['180'][i])), "".join(map(str, result['270'][i])))