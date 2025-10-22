import sys

input = sys.stdin.readline

N = int(input())
card_list = list(map(int, input().split()))

M = int(input())
num_list = list(map(int, input().split()))

card_counts = {}
for card in card_list:
    if card in card_counts:
        card_counts[card] += 1
    else:
        card_counts[card] = 1

result = []
for num in num_list:
    result.append(card_counts.get(num, 0))

print(*result)