# linear time solution
# def next_greatest_letter(letters, target):
#     for l in letters:
#         if l > target:
#             return l
#     return letters[0]

#log n time attempt // binary search

def next_greatest_letter(letters, target):
    while len(letters) > 0:
        if letters[len(letters)//2] > target:
            letters = letters[0:len(letters)//2]
        else:
            letters = letters[len(letters)//2:]
    return letters

print(next_greatest_letter(["c", "f", "j"], 'e'))
