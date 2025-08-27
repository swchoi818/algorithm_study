#print("         ,r\'\"7\nr`-_   ,'  ,/\n \\. \". L_r'\n   `~\\/\n      |\n      |")

# piece_cnt = [1, 1, 2, 2, 2, 8]

# piece = list(map(int, input().split()))

# for i in piece_cnt:

N = 1000000
isPrime = [True]*N
isPrime[0] = False
isPrime[1] = False
for i in range(2, int(N**0.5) + 1):
    if isPrime[i]:
        for j in range(i + i, N, i):
            isPrime[j] = False
        


T = int(input())
even_num = []
for tc in range(T):
    even_num.append(int(input()))

result = []
count = 0
for n in range(T):
    a = int(even_num[n]/2)
    for i in range(a, 0, -1):
        if isPrime[i] and isPrime[even_num[n] - i]:
            count += 1
    result.append(count)
    count = 0
print(*result,sep='\n')


    
    

