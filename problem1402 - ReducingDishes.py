def reducing_dishes(satisfaction): 
    satisfaction.sort()
    results = 0
    negative = []
    increment = 0

    for i in range(len(satisfaction)-1, -1, -1):
        if satisfaction[i] < 0:
            negative.insert(0, satisfaction.pop(i))
        else:
            increment += satisfaction[i]

    for i in range(0, len(satisfaction)):
        if satisfaction[i] >= 0:
            results += (i+1) * satisfaction[i]

    multiplier = 1
    for i in range(0, len(negative)):
        if abs(multiplier * negative[i]) < increment:
            results += increment + multiplier * negative[i]
            multiplier +=1

    return results

test = [-5,-7,8,-2,1,3,9,5,-10,4,-5,-2,-1,-6]
print(reducing_dishes(test))

    
    



        