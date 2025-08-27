factor = []

def primeFactor(a):
    for i in range(2, a + 1):
        if a%i == 0:
            factor.append(i)
            j = a//i
            return primeFactor(j)
            

n = int(input())
primeFactor(n)

print(*factor,sep="\n")
