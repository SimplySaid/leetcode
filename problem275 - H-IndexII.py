#Correct but can this be done using binary search?

# def hIndex (citations):
#     counter = 0
#     for i in range (len(citations)-1, -1, -1):
#         if citations[i] >= counter + 1:
#             counter += 1
#         else:
#             break
#     return counter

# input = [0,1,3,5,6,7]

# print(hIndex(input))


# def hIndex (citations):
#     left = 0; right = len(citations) - 1; mid = len(citations)

#     while right >= left:
#         mid = left + ((right - left) // 2)
#         if citations[mid] <= mid + 1:
#             left = mid + 1
#         else:
#             right = mid - 1

#         print('mid ' + str(mid), ' left'+  str(left) + ' right' + str(right))

#     return mid

def hIndex(citations):
    n = len(citations)
    l, r = 0, n-1
    while l <= r:
        mid = (l+r)/2
        if citations[mid] >= n-mid:
            r = mid - 1
        else:
            l = mid + 1
    return n-l

input = [0,1,3,5,6,7]
print(hIndex(input))