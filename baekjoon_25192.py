import sys

input = sys.stdin.readline

N = int(input())

user_set = set()
result = 0
for _ in range(N):
    user_name = input().rstrip()
    if user_name == "ENTER":
        result += len(user_set)
        user_set.clear()
    else:
        user_set.add(user_name)
else:
    result += len(user_set)
print(result)
