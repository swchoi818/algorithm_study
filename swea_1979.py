T = int(input())
 
for test_case in range(1, T + 1):
    N, K = map(int,input().split())
    word_puzzle = []
    for _ in range(N):
        word_puzzle.append((''.join(input().split())))
    cnt_list = []
    for i in word_puzzle:
        cnt_list.extend(list(map(str,i.split('0'))))
    kcnt = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if word_puzzle[j][i] == '1':
                cnt += 1
            if word_puzzle[j][i] == '0':
                if cnt == K:
                    kcnt += 1
                cnt = 0
        if cnt == K:
            kcnt += 1
            
    print(f"#{test_case}",cnt_list.count('1'*K) + kcnt)
        
    