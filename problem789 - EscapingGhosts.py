import math

def escape_ghosts(ghosts,target):
    p_distance = distance(0,0,target[0], target[1])
    for g in ghosts:
        if distance(g[0], g[1], target[0], target[1]) <= p_distance:
            return False
    return True

def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

game_ghosts = [[2, 0]]
tar = [1,0]

print(escape_ghosts(game_ghosts,tar))