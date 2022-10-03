#!/usr/bin/python3
def find_max(nums):
    max_num = float("-inf")  # smaller than all other numbers
    for num in nums:
        if num > max_num:
            max_num = num
            return max_num


nums = (3, 2, 1)
print(find_max(nums))
