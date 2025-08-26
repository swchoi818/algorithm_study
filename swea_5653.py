# 세포 클래스 생성
# 생명력 수치, 위치, 활성화/비활성화 상태
# 위치를 기준으로 해당 세포의 생명력 수치를 알 수 있어야 한다.
# 시간 흐름 -> 각 세포의 상태 확인/변경 -> 새로운 세포 생성
# 세포의 위치를 담은 집합 생성, 위치를 기준으로 찾을 수 있도록 세포의 정보는 위치를 키로 가지는 딕셔너리에 담는다. 입력 받은 정보 기준 초기 dict 생성, 추후에 새로운 세포 생성 시 추가
# 비활성화 세포 집합 -> 활성화 된 세포 집합 -> 죽은 세포 집합 동작도 이거 따라서 하면 될듯?

# 반복문 -> 비활성화 세포 timer -1 -> 0 되면 활성화로 변경 -> 활성화 된 세포 증식 -> 겹치는 위치 판별 큰 값으로 증식 -> 증식 완료 하면 죽은 세포 집합으로 이동

# 결과는 활성 세포 수 + 비활성 세포

# 세포 증식 함수? 비활성 대기 함수
# 세포 클래스
class Cell:
    def __init__(self, locate, vitality):
        self.is_activ = False
        self.locate = locate
        self.vitality = vitality
        self.time = vitality

    def wait_time(self):
        self.time -= 1
        if self.time == 0:
            self.is_activ = True
            return True
        return False

    def vital_decrease(self):
        self.vitality -= 1
        if self.vitality == 0:
            return True
        return False


dir_4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# 세포 증식 함수
def increase(cell):
    global inc_tmp, wait_cell, active_cell, death_cell
    cell.is_activ = False
    for dy, dx in dir_4:
        nx, ny = cell.locate[1] + dx, cell.locate[0] + dy
        if (ny, nx) in wait_cell or (ny, nx) in  death_cell or (ny, nx) in active_cell:
            continue
        if (ny, nx) in inc_tmp:
            inc_tmp[(ny, nx)].vitality = max(inc_tmp[(ny, nx)].vitality, cell.vitality)
            inc_tmp[(ny, nx)].time = inc_tmp[(ny, nx)].vitality
            continue
        inc_tmp[(ny, nx)] = Cell((ny, nx), cell.vitality)


T = int(input())

for t in range(1, T + 1):
    N, M, K = map(int, input().split())
    cell_mtr = [list(map(int, input().split())) for _ in range(N)]
    cell_dict = {}  # 세포 정보를 담을 dict
    wait_cell = set()  # 비활성화 세포 집합
    active_cell = set()  # 활성화 세포 집합
    death_cell = set()  # 죽은 세포 집합
    for i in range(N):
        for j in range(M):
            if cell_mtr[i][j] != 0:
                cell_dict[(i, j)] = Cell((i, j), cell_mtr[i][j])
                wait_cell.add((i, j))
    inc_tmp = {}
    for _ in range(K):
        # 활성화 된 세포 증식, 세포 생명력 -1, 처음 활성화된 세포는 is_activ -> True 증식 후 False 로 변경(increase 함수 참고)
        set_tmp = active_cell.copy()
        for cell in active_cell:
            if cell_dict[cell].is_activ:
                increase(cell_dict[cell])
            if cell_dict[cell].vital_decrease():
                death_cell.add(cell)
                set_tmp.discard(cell)
        active_cell = set_tmp.copy()

        # 비활성 세포 대기 시간 -1
        set_tmp = wait_cell.copy()
        for cell in wait_cell:
            if cell_dict[cell].wait_time():
                active_cell.add(cell)
                set_tmp.discard(cell)
        wait_cell = set_tmp.copy()

        cell_dict.update(inc_tmp)
        wait_cell.update(inc_tmp.keys())

        inc_tmp.clear()

    result = len(active_cell) + len(wait_cell)
    print(f"#{t}", result)
