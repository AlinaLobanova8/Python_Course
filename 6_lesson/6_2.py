_ = input()
nums = [int(i) for i in input().split()]

count = 0
for i in range(1, len(nums) - 1):
    if nums[i] == max(nums[i - 1: i + 2]):
        count += 1

print(count)