#Broken because loop is broken.. doesn't populate all the way yet...

def predictTheWinner (nums):
    dp = []

    for i in range (0, len(nums)):
        dp.append([])
        for j in range (0, len(nums)):
            dp[i].append((0,0))
        
    for i in range (0, len(nums)):
        dp[i][i] = (nums[i], 0)

    for i in range (0, len(dp)-1):
        for j in range (0, len(dp[i])):
            if dp[i][j] == (0,0):
                if nums[i] + dp[i+1][j][1] >= nums[j] + dp[i][j-1][1]:
                    dp[i][j] = (nums[i] + dp[i+1][j][1],dp[i+1][j][0])
                else:
                    dp[i][j] = (nums[j] + dp[i][j-1][1],dp[i][j-1][0])

    #return dp[0][len(nums)-1][0] >= dp[0][len(nums)-1][1]
    return dp

nums = [1,5,233,7]

print(predictTheWinner(nums))