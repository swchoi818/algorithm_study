def prime_factorization(f, n = 0, cnt = 0):
    global N
    if n == 0:
        n = N
    if n % f == 0:
        return prime_factorization(f, n//f, cnt + 1)
    return cnt


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    prime_list = [2, 3, 5, 7, 11]
    result = list(map(prime_factorization, prime_list))

    print(f"#{t}", *result)
