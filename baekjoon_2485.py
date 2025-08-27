import sys

input = sys.stdin.readline

def get_GCD(a, b):
    if a < b:
        a, b = b, a
    a %= b
    if a == 0:
        return b
    return get_GCD(b, a)

N = int(input())
spacce_list = []
locate_tree_1 = int(input())
gcd_value = 0
for i in range(1, N):
    locate_tree_2 = int(input())
    spacce_list.append(locate_tree_2 - locate_tree_1)
    locate_tree_1 = locate_tree_2
    if i == 1:
        gcd_value = get_GCD(spacce_list[i-2], spacce_list[i-1])
    else:
        gcd_value = get_GCD(gcd_value, spacce_list[i-1])
result = 0
for i in spacce_list:
    result += ((i//gcd_value) - 1)

print(result)