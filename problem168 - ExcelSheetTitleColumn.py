def convert_to_title(n):
    results = ''
    while n > 0:
        results = results + chr(n%26+65)
        n = n//26
    return results

print(convert_to_title(701))
