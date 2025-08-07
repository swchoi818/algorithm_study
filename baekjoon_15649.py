import sys

input = sys.stdin.readline

N, M = map(int,input().split())

result = []

def search_num(next_choice, selected_num = []):
    global result
    if len(selected_num) == M:
        result.append(selected_num[:])
    
    for i in next_choice:
        selected_num.append(i)
        nxtchc = next_choice[:]
        nxtchc.remove(i)
        search_num(nxtchc, selected_num)
        selected_num.pop()

search_num(list(range(1,N+1)))
for i in result:
    print(*i, sep = ' ')
