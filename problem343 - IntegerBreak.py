#Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. 
# Return the maximum product you can get.

def integerBreak(n):
    bits = []
    results = 1

    if n <= 3:
        return n - 1

    while n > 0:
        if n >= 3 and n != 4:
            n = n - 3
            bits.append(3)
        elif n == 4:
            n = n - 2
            bits.append(2)
        else:
            bits.append(n)
            n = n - n

    for b in bits:
        results *= b
    
    return results

print(integerBreak(15))