def largestTimeFromDigits(A):
    A.sort()
    result = ""

    for i in range(len(A) - 1, 0, -1):
        if int(str(A[i]) + str (A[i-1])) < 24:
            result += str(A[i]) + str(A[i-1]) + ":"
            A.pop(i)
            A.pop(i-1)
            break
    if A[0] > A[1]:
        result += str(A[0]) + str(A[1])
    else:
        result += str(A[1]) + str(A[0])

    if len(result) == 5:
        return result
    else:
        return "" 

input = [5,5,5,5]
print(largestTimeFromDigits(input))


