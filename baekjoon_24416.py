def fibonacci(n):
    global cnt2
    f = [0] * n
    f[0] = f[1] = 1
    for i in range(2, n):
        f[i] = f[i - 1] + f[i - 2]
        cnt2 += 1
    return f[n - 1]


def fib(n):
    global cnt1
    if n == 1 or n == 2:
        cnt1 += 1
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


N = int(input())
cnt1 = 0
cnt2 = 0
fib(N)
fibonacci(N)
print(cnt1, cnt2)
