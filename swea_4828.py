import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))
    print(f"#{i + 1} {max(num_list) - min(num_list)}")
        
