#Idea.. match as many letters as possible, then check for "stretches"

def group_string(S):
    group = [[S[0],1]]
    for i in range (1, len(S)):
        if S[i] == S[i-1]:
            group[-1][1] += 1
        else:
            group.append([S[i],1])
    return group

def expressiveWords(S, words):
    grouped_string = group_string(S)
    result = 0

    for w in words:
        temp = group_string(w)
        for i in range(0, len(grouped_string)):
            if temp[i][0] != grouped_string[i][0] or (temp[i][1] != grouped_string[i][1] and grouped_string[i][1] < 3):
                break
            if i == len(grouped_string) - 1:
                result += 1
    return result

test_s = "heeellooo"
words = ["hello", "hi", "helo"]

print(expressiveWords(test_s,words)) 