def checkRecord(s):
    l, a = 0,0

    for i in range (0, len(s)):
        if s[i] == "A":
            a += 1     
        if s[i] == "L":
            l += 1
        else:
            l = 0

        if l >= 3 or a >= 2:
            return False
            
    return True

input = "PPALLL"

print(checkRecord(input))