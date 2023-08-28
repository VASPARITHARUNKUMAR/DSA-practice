def has_subarray_with_0_sum(nums):
    cumulative_sum = 0
    sum_map = {}  # Store cumulative sums and their indices
    
    for i in range(len(nums)):
        cumulative_sum += nums[i]
        
        # Case 1: Found a subarray with sum 0
        if cumulative_sum == 0 or nums[i] == 0 or cumulative_sum in sum_map:
            return True
        
        sum_map[cumulative_sum] = i
        
    return False

# Example usage
nums = [4, 2, -3, 1, 6]
has_zero_sum_subarray = has_subarray_with_0_sum(nums)
print("Does the array have a subarray with 0 sum?", has_zero_sum_subarray)
