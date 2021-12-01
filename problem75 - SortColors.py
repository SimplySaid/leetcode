def sortColors(nums):
    left = 0
    right = len(nums) - 1
    
    for i in range (0, nums):
        if nums[i] == 2:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1
        if nums[i] == 0:
            


