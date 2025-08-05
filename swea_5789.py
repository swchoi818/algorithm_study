T = int(input())
 
for test_case in range(1, T + 1):
    N, Q = map(int,input().split())
    result = [0]*N
    for i in range(Q):
        L, R = map(int,input().split())
        for j in range(L - 1,R):
            result[j] = i + 1
     
    print(f"#{test_case}",*result,sep=' ')
    