def find_min_in_rotated_array(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        middle = left + (right - left) // 2
        
        if nums[middle] > nums[right]:
            left = middle + 1
        else:
            right = middle
    
    return nums[left]
rotated_array = [4, 5, 6, 7, 0, 1, 2]
minimum = find_min_in_rotated_array(rotated_array)
print("The minimum element is:", minimum)
