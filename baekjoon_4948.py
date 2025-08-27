prime_ran = 123456 * 2
prime_list = [True]*(prime_ran + 1)
prime_list[0] = False
prime_list[1] = False

for i in range(2,int(prime_ran**0.5) + 1):
    if prime_list[i]:
        for j in range(i+i,prime_ran + 1,i):
            prime_list[j] = False

while True:
    n = int(input())
    cnt = 0
    if n == 0:
        break
    for i in range(n+1,(n*2)+1):
        if prime_list[i]:
            cnt += 1
    print(cnt)