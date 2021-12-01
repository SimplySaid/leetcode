# def findLHS (nums):
#     results = 0
#     for i in range (0, len(nums)):
#         curr_count = 0
#         for j in range(0, len(nums)):
#             if nums[j] <= nums[i] <= nums[j] + 1:
#                 curr_count +=1
#         if curr_count > results:
#             results = curr_count
#     return results

# quadratic time... can I shorten this?
# can use sort for n(log n).. any other solutions?

#def findLHS(nums):

#O(2n)
def findLHS(nums):
    counter = {}
    results = 0
    for n in nums:
        counter[n] = counter.get(n, 0) + 1
    
    for x in counter:
        if x+1 in counter:
            results = max(results, counter[x] + counter[x+1])
    return results

num = [1,1,1,1]
print(findLHS(num))
