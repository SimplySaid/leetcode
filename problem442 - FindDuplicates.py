# def findDuplicates(nums):
#     stack, results = [], []
#     for n in nums:
#         if n in stack:
#             results.append(n)
#         else:
#             stack.append(n)
#     return results

#is in inefficient?

from collections import Counter

# def findDuplicates(nums):
#     results = Counter()
#     for n in nums:
#         results[n] += 1

#     return results

# def findDuplicates(nums):
#     results = []
#     counter = {}
#     for n in nums:
#         if n in counter.keys():
#             counter[n] += 1
#         else:
#             counter[n] = 1

#     for x, y in counter.items():
#         if y == 2:
#             results.append(x)
#     return results

def findDuplicates(nums):
    res = []
    for x in nums:
        print(nums)
        print(res)
        if nums[abs(x)-1] < 0:
            res.append(abs(x))
        else:
            nums[abs(x)-1] *= -1
    return res

test_nums = [4,3,2,7,8,2,3,1]

print(findDuplicates(test_nums))
