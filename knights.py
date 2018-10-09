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

    if not (currentpos[0] > 8 or currentpos[0] < 1 or currentpos[1] > 8 or currentpos[1] < 1):
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


def findpathhelp(item, paths=[], pathlst=[]):
    #findpathhelp(start)
    #findpathhelp('end')
    if item == 'end':
        paths.append(pathlst)
    elif item == 'path':
        return paths
    else:
        pathlst.append(item)

def findpath(start, pawns):
    solvable(start, pawns)
    paths = findpathhelp('path')
    return paths

def findstart(pawns):
    board = []
    startingpoints = []
    for i in range(8):
        for j in range(8):
            board.append((i+1, j+1))
    for item in board:
        if solvable(item, pawns) and item not in pawns:
            startingpoints.append(item)
    return set(startingpoints)
