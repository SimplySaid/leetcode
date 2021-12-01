def min_deletion_size(A):
    results = 0
    for i in range(0, len(A[0])):
        for j in range (i, len(A[0])):
            for k in range (1, len(A)):
                
