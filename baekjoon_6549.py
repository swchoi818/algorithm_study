import sys

input = sys.stdin.readline


def divide_conquer(low, high, histo):
    if high <= low:
        return histo[low]
    mid = ((high - low) // 2) + low
    left_max = divide_conquer(low, mid, histo)
    right_max = divide_conquer(mid + 1, high, histo)

    middle_max = get_max_square(low, high, mid, mid + 1, histo)

    return max(left_max, middle_max, right_max)


def get_max_square(low, high, left, right, histo):
    max_square = min(histo[left], histo[right]) * 2
    height = min(histo[left], histo[right])
    while left > low or right < high:
        if left > low and right < high:
            if histo[left - 1] < histo[right + 1]:
                right += 1
                height = min(height, histo[right])
            else:
                left -= 1
                height = min(height, histo[left])
        elif left > low:
            left -= 1
            height = min(height, histo[left])
        elif right < high:
            right += 1
            height = min(height, histo[right])
        max_square = max(max_square, height * (right - left + 1))

    return max_square


while True:
    histogram = list(map(int, input().split()))
    if histogram == 0:
        exit(0)
    print(divide_conquer(0, histogram[0] - 1, histogram[1:]))




