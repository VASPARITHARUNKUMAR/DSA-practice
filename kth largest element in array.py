def find_kth_largest(nums, k):
    nums.sort()
    return nums[len(nums) - k]
nums = [3, 2, 1, 5, 4, 6]
k = 2
kth_largest = find_kth_largest(nums, k)
print(f"The {k}th largest element is:", kth_largest)
