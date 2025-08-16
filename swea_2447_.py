# 접수창구로 고객이 들어오는 부분
# 창구가 비어 있는지 확인 -> customer list에 해당 인덱스에 접수 창구 번호 추가
# 창구 클래스의 해당 고객의 인덱스를 입력 -> 업무가 끝나면 반환
# timer 매소드 작성 -> start_work 매소드 호출 시 상태 변환

# 상태에 따라 업무 진행 (timer -1) 0이면 해당 고객 번호와, 창구 번호를 반환
# 업무가 끝났는지 반환 -> 접수 창구 순회

# 정비 창구 -> 접수 창구에서 반환 된 값을 보고 비어 있는 정비 창구에 입력
# 비어있는 정비창구가 없다면? -> wait 리스트에 넣어서 대기 wait에 고객 번호를 넣음
# 해당 창구에 번호를 customer list에 해당 인덱스에 append

# Desk 클래스 -> 창구 번호, 업무 처리 시간, 현재 상태, 비어 있는지 여부
# -> 매소드 -> work_start, timer, is_worknig
from collections import deque

class Desk:
    def __init__(self, work_time):
        self.work_time = work_time
        self.is_working = False
        self.timer = work_time
        self.customer_num = -1

    def start_work(self, customer_num):
        self.customer_num = customer_num
        self.is_working = True

    def working(self):
        self.timer -= 1
        if self.timer == 0:
            self.timer = self.work_time
            self.is_working = False
        return self.is_working
    


def find_enpty_desk(desk, n, cus_num):
    for i in range(n):
        if not desk[i].is_working:
            desk[i].start_work(cus_num)
            return i
    return -1


T = int(input())

for t in range(1, T + 1):
    N, M, K, A, B = map(int, input().split())
    reception_desk = list(map(Desk, list(map(int, input().split()))))
    repair_desk = list(map(Desk, list(map(int, input().split()))))
    wait_deque = deque()
    customer_list = list(map(int, input().split()))
    rec_cus_result = [-1] * K
    rep_cus_result = [-1] * K
    now_time = -1
    is_end = False
    while not is_end:
        now_time += 1
        # 접수 창구에 고객을 배정
        for i in range(K):
            if 0 <= customer_list[i] <= now_time:
                desk_num = find_enpty_desk(reception_desk, N, i)
                if desk_num != -1:
                    customer_list[i] = -1
                    rec_cus_result[i] = desk_num
        # 고객이 있는 접수 창구는 업무 수행
        # 업무가 끝나면 비어 있는 정비 창구 업무 시작
        # 비어있는 업무 창구가 없다면 wait 리스트에 추가
        for desk in reception_desk:
            if desk.is_working:
                if not desk.working():
                    desk_num = find_enpty_desk(repair_desk, M, desk.customer_num)
                    if desk_num != -1:
                        rep_cus_result[desk.customer_num] = desk_num
                    else:
                        wait_deque.append(desk.customer_num)
        # 정비 창구 업무 수행, 업무가 끝난 정비 창구가 있다면 wait_deque에 고객을 확인하여 배정
        for i in range(M):
            if repair_desk[i].is_working:
                if not repair_desk[i].working():
                    if len(wait_deque):
                        repair_desk[i].start_work(wait_deque.popleft())
                        rep_cus_result[repair_desk[i].customer_num] = i
        # 종료 조건 판단
        if -1 not in rep_cus_result:
            is_end = True

    result = -1
    # 조건에 해당하는 고객 번호 계산
    for i in range(K):
        if rec_cus_result[i] + 1 == A and rep_cus_result[i] + 1 == B:
            result += i + 1
    if result != -1:
        result +=1
    print(f"#{t} {result}")