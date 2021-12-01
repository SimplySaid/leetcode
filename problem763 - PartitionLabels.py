##Incomplete Error in Code

def partitionLabels(S):
    last_positions = {}
    partitions = []

    #Get last position for each character
    for i in range (0, len(S)):
        last_positions[S[i]] = i + 1

    current_index = 0

    while current_index < len(S):
        index_end = last_positions[S[current_index]]
        for i in range (current_index, index_end):
            if last_positions[S[i]] > index_end:
                index_end = last_positions[S[i]]
        partitions.append(len(S[current_index:index_end]))
        current_index = index_end

    return partitions

test_str = 'ababcbacadefegdehijhklij'

print(partitionLabels(test_str))