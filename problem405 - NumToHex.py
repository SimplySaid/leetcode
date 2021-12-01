def num_to_hex (n):
    res = ''
    while n > 0:
        r = n%16
        if n%16 >= 10:
            r = chr(65 + (r - 10))
        res = str(r) + res
        n = n // 16
    return res

print(num_to_hex(3000))