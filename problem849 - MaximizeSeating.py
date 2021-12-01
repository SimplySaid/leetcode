import math

def maxDistToClosest(seats):
    curr = 0
    results = 0
    for s in seats:
        if s == 0:
            curr += 1
        else:
            if (curr + 1) // 2 > results:
                results = (curr + 1) // 2
            curr = 0
    if curr > results:
        results = curr
    return results

s = [0,1]

print(maxDistToClosest(s))