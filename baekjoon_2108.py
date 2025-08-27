import sys

input = sys.stdin.readline

N = int(input())
num_list = []

for i in range(N):
    num_list.append(int(input()))

num_list.sort()
count_same={}

for i in num_list:
    try: count_same[i] += 1
    except: count_same[i]=1

m = max(count_same.values())
mc = list(count_same.values()).count(m)
mi =  0

for i in count_same.keys():
    if count_same[i] == m and mc == 1:
        m = i
        break
    if count_same[i] == m:
        if mi == 1:
            m = i
            break
        mi += 1
        
print(round(sum(num_list)/N))
print(num_list[N//2])
print(m)
print(abs(num_list[0] - num_list[N-1]))