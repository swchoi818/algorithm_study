T = int(input())

for test_case in range(1, T + 1):
    input()
    One_set = set(input().split('0'))
    
    print(f"#{test_case} {max(list(map(len,One_set)))}")