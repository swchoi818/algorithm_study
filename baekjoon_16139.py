S = input()
q = int(input())
q_list = [list(input().split()) for _ in range(q)]

result = []

cnt = 0
cnt_dict = {}
for i in range(ord('a'), ord('z') + 1):
    cnt_dict[chr(i)] = 0
cnt_list = [cnt_dict.copy()]
for i in S:
    cnt_dict = cnt_list[len(cnt_list) - 1].copy()
    cnt_dict[i] += 1
    cnt_list.append(cnt_dict.copy())
for q in q_list:
    result.append(cnt_list[int(q[2]) + 1][q[0]] - cnt_list[int(q[1])][q[0]])

print(*result, sep='\n')
