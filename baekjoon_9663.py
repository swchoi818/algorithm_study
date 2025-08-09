N = int(input())

cnt = 0

def set_queen(rank, files = set(), diag1 = set(), diag2 = set()):
    global cnt
    if rank == N:
        cnt += 1
        return
    
    for i in range(N):
        if not ((i in files) or ((i - rank) in diag1) or ((i + rank) in diag2)):
            files.add(i)
            diag1.add(i - rank)
            diag2.add(i + rank)
            rank += 1
            set_queen(rank, files, diag1, diag2)
            rank -= 1
            files.discard(i)
            diag1.discard(i - rank)
            diag2.discard(i + rank)
    return

set_queen(0)

print(cnt)