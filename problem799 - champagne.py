def champagneTower (self, poured, query_row, query_glass):
    glasses = [poured]
    for i in range (1, query_row):
        for j in range (0, i+1):
            glasses[i].append(glasses[i-1])

