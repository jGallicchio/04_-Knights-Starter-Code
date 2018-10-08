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

def ispawn(moves, pawns):
    valmoves = []
    for pos in moves:
        spot = tuple(pos)
        if spot in pawns:
            pawns.remove(spot)
            valmoves.append(spot)
            #return True
            #return False
    return valmoves

def movepos(pos):
    moves = []
    turns = [-1, 1]
    directions = ['up', 'down', 'left', 'right']
    for item in directions:
        #print(item)
        for num in turns:
            #print(num)
            move = canmove(pos, item, num)
            #print(move)
            if(move):
                #print('hi')
                moves.append(move)
    #print(moves)
    return moves

def solvable(start, pawns):
    possible = False
    if(len(pawns) == 0):
        possible = True
    elif start is None:
        pass
    else:
        pos = list(start)
        moves = movepos(pos)
        posmoves = ispawn(moves, pawns)
        print(posmoves)
        for item in posmoves:
            solvable(item, pawns)
    return possible
start = [5, 6]
pawns = {(4, 3), (6, 5), (7, 7)}
print(solvable(start, pawns))
