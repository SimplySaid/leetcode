# def kWeakestRows(mat, k):
#     result = []
#     for m in mat:
#         subcount = 0
#         for e in m:
#             if e == 1:
#                 subcount += 1
#         result.append(subcount)
#     return result

# print(kWeakestRows(mat,k))

#More optimized solution

def kWeakestRows(mat, k):
    result = []
    for m in mat:
        right, left = len(m) - 1, 0
        while right > left:
            if m[(right-left)//2] == 1:
                if m[(right-left)//2-1] == 0:
                    break
                left = (right - left)//2
            else:
                right = (right - left)//2

        result.append((right-left)//2)
    return result

mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]

k = 3

print(kWeakestRows(mat, k))