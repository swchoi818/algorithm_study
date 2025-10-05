def binary_search(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

N = int(input())
num_list = list(map(int, input().split()))
M = int(input())
target_num_list = list(map(int, input().split()))

num_list.sort()

for i in target_num_list:
    print(binary_search(num_list, i))
