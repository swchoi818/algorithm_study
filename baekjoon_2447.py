import sys

input = sys.stdin.readline

def make_star(n):
    if n//3 == 0:
        return '*'
    star_list = make_star(n//3)
    result = []
    for i in star_list:
        result.append(i*3)
    for i in star_list:
        result.append(i + " "*(n//3) + i)
    for i in star_list:
        result.append(i*3)
    
    return result

n = int(input())

print(*make_star(n),sep='\n')
