import sys

input = sys.stdin.readline

N = int(input())

people_set = set()
is_dance = False
result_set = set()
for _ in range(N):
    people_set = set(input().split())
    if people_set & {'ChongChong'} == {'ChongChong'}:
        is_dance = True
        result_set = result_set.union(people_set)
    if is_dance and result_set & people_set:
        result_set = result_set.union(people_set)

print(len(result_set))