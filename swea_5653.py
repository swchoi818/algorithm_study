# 세포 클래스 생성
# 생명력 수치, 위치, 활성화/비활성화 상태
# 위치를 기준으로 해당 세포의 생명력 수치를 알 수 있어야 한다.
# 시간 흐름 -> 각 세포의 상태 확인/변경 -> 새로운 세포 생성
# 세포의 위치를 담은 집합 생성, 위치를 기준으로 찾을 수 있도록 세포의 정보는 위치를 키로 가지는 딕셔너리에 담는다. 입력 받은 정보 기준 초기 dict 생성, 추후에 새로운 세포 생성 시 추가
# 비활성화 세포 집합 -> 활성화 된 세포 집합 -> 죽은 세포 집합 동작도 이거 따라서 하면 될듯?

# 반복문 -> 비활성화 세포 timer -1 -> 0 되면 활성화로 변경 -> 활성화 된 세포 증식 -> 겹치는 위치 판별 큰 값으로 증식 -> 증식 완료 하면 죽은 세포 집합으로 이동

# 결과는 활성 세포 수 + 비활성 세포

# 세포 증식 함수? 비활성 대기 함수
class Cell:
    def __init__(self, health, locate):
        self.health = health
        self.locate = locate
        self.wait_time = health

    def waiting(self):
        self.wait_time -= 1
        if self.wait_time == 0:
            self.wait_time = self.health
            return True
        return False
    

dir_4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def increase_cell(cell):
    y = cell.locate[0]
    x = cell.locate[1]
    for dy, dx in dir_4:
        ny = y + dy
        nx = x + dx
        if (ny, nx) not in (active_cell + wait_cell + death_cell):
            if (ny, nx) in inc_cell:
                cell_dict[(ny, nx)].health = max(cell_dict[(ny, nx)].health, cell_dict[(y, x)].health)
            else:
                cell_dict[(ny, nx)] = Cell(cell_dict[(y, x)], (ny, nx))
                inc_cell.add((ny, nx))
    return inc_cell


T = int(input())

for t in range(1, T + 1):
    N, M, K = map(int, input().split())
    cell_mtr = [list(map(int, input().split())) for _ in range(N)]
    cell_dict = {}
    wait_cell = set()
    active_cell = set()
    death_cell = set()
    inc_cell = set()
    for i in range(N):
        for j in range(M):
            if cell_mtr[i][j] != 0:
                cell_dict[(i, j)] = Cell(cell_mtr[i][j], (i, j))
                wait_cell.add((i, j))

    for _ in range(K):
        tmp = set()
        for activ_key in active_cell:
            if cell_dict[activ_key].wait_time == cell_dict[activ_key].health:
                wait_cell.union(increase_cell(cell_dict[activ_key]))
            if cell_dict[activ_key].waiting():
                tmp.add(activ_key)

        tmp2 = set()
        for wait_key in wait_cell:
            if cell_dict[wait_key].waiting():
                tmp2.add(wait_key)
    
        active_cell = active_cell - tmp
        death_cell.union(tmp)
        
        wait_cell = wait_cell - tmp2
        active_cell.union(tmp2)

    print(f"#{t} {len(wait_cell) + len(active_cell)}")
