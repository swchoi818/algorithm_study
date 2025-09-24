N = int(input())

dist_list = list(map(int, input().split()))
charge_list = list(map(int, input().split()))

result = 0
min_charge = charge_list[0]
for i in range(N - 1):
    min_charge = min(min_charge, charge_list[i])
    result += dist_list[i] * min_charge

print(result)

