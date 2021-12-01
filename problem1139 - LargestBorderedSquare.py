def largest1BorderedSquare(grid):
    largestSquare = 0
    for i in range (0, len(grid)):
        for j in range (0, len(grid[i])):
            if grid[i][j] == 1:
                for k in range (min(len(grid), len(grid[i])-1), -1, -1):
                    if grid[k][k] == 1:
                        #check all borders


grid = [[1,1,1],[1,0,1],[1,1,1]]
largest1BorderedSquare(grid)