def canIWin(maxChoosableInteger, desiredTotal):
    if maxChoosableInteger + maxChoosableInteger - 1 >= desiredTotal + 1:
        return True
