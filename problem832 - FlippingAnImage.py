def flipAndInvertImage (A):
    results = []

    for i in range (0, len(A)):
        results.append([])
        for j in range (len(A[i])-1, -1, -1):
            if A[i][j] == 0:
                results[i].append(1)
            else:
                results[i].append(0)
    return results

test = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]

print(flipAndInvertImage(test))
