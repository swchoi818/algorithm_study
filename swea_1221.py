num_dict = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}

def str_to_num(numstr):
    return num_dict[numstr]
     
def num_to_str(num):
    return [key for key, value in num_dict.items() if value == num].pop()

T = int(input())

for test_case in range(1, T + 1):
    input()
    num_list = list(map(str_to_num, input().split()))
    
    num_list.sort()
    
    print(f"#{test_case}")
    print(*list(map(num_to_str, num_list)), sep=" ")