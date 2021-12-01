#Wrong

def pivotIndex(nums):
    l_index, r_index = 0, len(nums) -1
    l, r = 0, 0

    if len(nums) == 0:
        return -1

    while l_index +1 <= r_index:
        if l <= r:
            if nums[l_index] >= 0:
                l += nums[l_index]
                l_index += 1
            else:
                r += nums[r_index]
                r_index -= 1
        else:
            if nums[r_index] >= 0:
                print('test' + str(r))
                print('test' + str(r_index))
                r += nums[r_index]
                r_index -= 1
                print('test' + str(r))
            else:
                l += nums[l_index]
                l_index += 1
        print(r_index)

    if l == r:
        return l_index
    else:
        return -1


nums = [-1,-1,0,-1,-1,0]
print(pivotIndex(nums))





