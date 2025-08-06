class Microbial:
    def __init__(self, mic_info):
        self.locate = [mic_info[0], mic_info[1]]
        self.num = mic_info[2]
        self.max_num = mic_info[2]
        self.dir = mic_info[3]

    def move(self):
        if self.dir == 1:
            self.locate[0] -= 1            
        elif self.dir == 2:
            self.locate[0] += 1
        elif self.dir == 3:
            self.locate[1] -= 1
        elif self.dir == 4:
            self.locate[1] += 1
        self.max_num = self.num
        return self.locate
    
    def meet_chemical(self):
        if self.dir == 1:
            self.dir = 2          
        elif self.dir == 2:
            self.dir = 1   
        elif self.dir == 3:
            self.dir = 4          
        elif self.dir == 4:
            self.dir = 3
        self.num //= 2
        self.max_num = self.num
        return self.num

    def merge_microb(self, mic):
        if self.max_num < mic.num:
            self.dir = mic.dir
            self.max_num = mic.num
        self.num += mic.num

    def __str__(self):
        return f"{self.locate} {self.num} {self.dir}"

T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int,input().split())
    microb_list = []
    for _ in range(K):
        microb_list.append(Microbial(list(map(int, input().split()))))
    for i in range(M):
        locate_dict = {}
        for microb in microb_list:
            if microb.num != 0:
                now_loc = tuple(microb.move())
                if (now_loc[0] == N - 1) or (now_loc[0] == 0) or (now_loc[1] == N - 1) or (now_loc[1] == 0):
                    microb.meet_chemical()
                try:
                    microb_list[locate_dict[now_loc]].merge_microb(microb)
                    microb.num = 0
                except:
                    locate_dict[now_loc] = microb_list.index(microb)
    result = 0
    for m in microb_list:
        result += m.num
    print(f"#{test_case}", result)
