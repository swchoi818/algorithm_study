from collections import deque


class Desk:
    def __init__(self, work_time):
        self.work_time = work_time
        self.is_empty = True
        self.timer = work_time + 1

    def start_work(self):
        self.is_empty = False
        self.timer -= 1
        if self.timer == 0:
            self.timer = self.work_time + 1
            self.is_empty = True
            return True
        return False


T = int(input())

for t in range(1, T + 1):
    N, M, K, A, B = map(int, input().split())
    reception_desk = list(map(Desk, list(map(int, input().split()))))
    repair_desk = list(map(Desk, list(map(int, input().split()))))
    rec_tmp = [-1 for _ in range(K)]
    rec_result = [-1 for _ in range(K)]
    rep_tmp = [-1 for _ in range(K)]
    rep_result = [-1 for _ in range(K)]
    is_end = False
    waiting_list = deque()
    customer_list = list(map(int, input().split()))
    now_time = -1
    while not is_end:
        now_time += 1
        for i in range(K):
            if 0 <= customer_list[i] <= now_time:
                for j in range(N):
                    if reception_desk[j].is_empty:
                        rec_tmp[i] = j
                        customer_list[i] = -1
                        reception_desk[j].start_work()
                        break
        
        for i in range(K):
            if rec_tmp[i] == -1:
                continue
            if reception_desk[rec_tmp[i]].start_work():
                rec_result[i] = rec_tmp[i]
                rec_tmp[i] = - 1
                for j in range(M):
                    if repair_desk[j].is_empty:
                        rep_tmp[i] = j
                        repair_desk[j].start_work()
                        break
                else:
                    waiting_list.append(i)
        for i in range(K):
            if rep_tmp[i] == -1:
                continue
            if repair_desk[rep_tmp[i]].start_work():
                rep_result[i] = rep_tmp[i]
                if len(waiting_list) != 0:
                    rep_tmp[waiting_list.popleft()] = rep_tmp[i]
                    repair_desk[rep_tmp[i]].start_work()
                rep_tmp[i] = - 1
                if -1 not in rep_result:
                    is_end = True
                    break

    result = 0

    print(rec_result)
    print(rep_result)
    for i in range(K):
        if rec_result[i] + 1 == A and rep_result[i] + 1 == B:
            result += i + 1
    if result == 0:
        result = -1

    print(f"#{t} {result}")