#Justin Gallicchio

def canmove(pos, direction, turn):
    currentpos = []
    if (direction == 'up'):
        currentpos.append(pos[0] + turn)
        currentpos.append(pos[1] + 2)
    elif (direction == 'down'):
        currentpos.append(pos[0] + turn)
        currentpos.append(pos[1] - 2)
    elif (direction == 'right'):
        currentpos.append(pos[0] + 2)
        currentpos.append(pos[1] + turn)
    elif (direction == 'left'):
        currentpos.append(pos[0] - 2)
        currentpos.append(pos[1] + turn)
    #print(currentpos)
    if (currentpos[0] > 8 or currentpos[0] < 1 or currentpos[1] > 8 or currentpos[1] < 1):
        return False
    else:
        return currentpos

def posmove(pos, pawns):
    moves = []
    turns = [-1, 1]
    directions = ['up', 'down', 'left', 'right']
    for item in directions:
        for num in turns:
            move = canmove(pos, item, num)
            #print(move)
            if move:
                possiblemove = tuple(move)
                if possiblemove in pawns:
                    moves.append(possiblemove)
    return moves

def ispawn(pos, pawns):
    if pos in pawns:
        pawns.remove(pos)
    return pawns

def solvable(start, pawns):
    result = set()
    moves = posmove(start, pawns)
    for item in moves:
        newpawn = set(pawns)
        newpawn = ispawn(item, newpawn)
        if len(newpawn) == 0:
            return True
        else:
            result.add(solvable(item, newpawn))
    return True in result

def findpath():
    pass

def findstart():
    pass

start = (1, 1)
pawns = {(2,2), (2,3), (2,4), (3,2), (3,4), (4,2), (4,3), (4,4), (5,5), (5,6), (5,7), (6,5), (6,7), (7,5), (7,6), (7,7)}
print(solvable(start, pawns))
