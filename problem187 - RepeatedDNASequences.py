def findRepeatedDnaSequences(s):
    sequences = {}
    results = []

    for i in range (0, len(s)-9):
        if s[i:i+10] in sequences.keys() and sequences[s[i:i+10]] == False:
            sequences[s[i:i+10]] = True
            results.append(s[i:i+10])
        else:
            sequences[s[i:i+10]] = False

    for key, value in sequences.items():
        if value > 1:
           results.append(key) 

    return results

input = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(findRepeatedDnaSequences(input))