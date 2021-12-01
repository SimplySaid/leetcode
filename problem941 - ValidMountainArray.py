def validMountainArray(A):
    status = 1
    for i in range (0, len(A)-1):
        if A[i] * status > A[i+1]:
            print('test')
            if status == -1:
                return False
            else:
                status = -1
        elif A[i] == A[i+1]:
                return False
    return True

input = [0,3,2,1]
print(validMountainArray(input))

