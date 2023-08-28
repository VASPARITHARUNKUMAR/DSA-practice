def max_non_negative_subarray(nums):
    start, end = 0, 0
    current_sum, max_sum = 0, 0
    
    for i in range(len(nums)):
        if nums[i] >= 0:
            current_sum += nums[i]
            if current_sum > max_sum:
                max_sum = current_sum
                end = i
        else:
            current_sum = 0
            start = i + 1
    
    return nums[start:end+1]

# Example usage
nums = [1, 2, 5, -7, 2, 3]
max_subarray = max_non_negative_subarray(nums)
print("Maximum non-negative subarray:", max_subarray)
