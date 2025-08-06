import sys

input = sys.stdin.readline

def cantor_set(dash_str, n):
    n //= 3
    if n == 0:
        return dash_str
    dash_str = dash_str[:n]
    return cantor_set(dash_str, n) + " "*n + cantor_set(dash_str, n)
    
while True:
    try:
        n = int(input())
        dash_str = '-'*(3**n)
        print(cantor_set(dash_str, 3**n))
    except:
        break



