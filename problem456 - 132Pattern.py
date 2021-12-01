# def find132pattern(nums):
#     current_pattern = nums[0:3]
#     for i in range (2, len(nums)):
#         if i != 2:
#             current_pattern = current_pattern[1:]
#             current_pattern.append(nums[i])
#         if current_pattern[0] < current_pattern[2] < current_pattern[1]:
#             return True
#     return False

# incorrect... doesn't take into account skips

def find132pattern(nums):
    min_left = 99999
    for i in range (0, len(nums) - 2):
        if nums[i] >= min_left:
            continue
        else:
            min_left = nums[i]
            for j in range (len(nums) -1, i+1, -1):
                if nums[j] > nums[i]:
                    for k in range (i+1, j+1):
                        if nums[k] > nums[j]:
                            return True
    return False


test = 
print(find132pattern(test))