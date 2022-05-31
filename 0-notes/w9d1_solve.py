import w9d1_maze as m


def solve():
    while not m.finished():
        if m.canGoLeft():
            m.left()
            m.forward()
        elif m.canGoForward():
            m.forward()
        elif m.canGoRight():
            m.right()
            m.forward()
        else:
            m.right()
            m.right()
            m.forward()
    
def left(dir):
    if dir == m.NORTH:
        return m.WEST
    if dir == m.WEST:
        return m.SOUTH
    if dir == m.SOUTH:
        return m.EAST
    if dir == m.EAST:
        return m.NORTH

def right(dir):
    return left(left(left(dir)))

def move(square, dir):
    (r, c) = square
    if dir == m.NORTH:
        return (r-1,c)
    if dir == m.WEST:
        return (r,c-1)
    if dir == m.SOUTH:
        return (r+1,c)
    if dir == m.EAST:
        return (r,c+1)

def solveDFS():
    path = getPath(m, (0,0), m.EAST)

LEFT = 0
FORWARD = 1
RIGHT = 2

def getPath(m, square, dir, seen):
    if square in seen:
        return None
    if m.finish(square) == True:
        return []

    if m.canGo(square, left(dir)):
        path = getPath(m, move(square, left(dir)), left(dir), seen | {square})
        if path is not None:
            return [LEFT] + path
    
    if m.canGo(square, dir):
        path = getPath(m, move(square, dir), dir)
        if path is not None:
            return [RIGHT] + path

    if m.canGo(square, right(dir)):
        path = getPath(m, move(square, right(dir)), right(dir), seen | {square})
        if path is not None:
            return [RIGHT] + path

    return None
    
def solveDFS():
    path = getPath(m, (0,0), m.EAST, {})
    for dir in path:
        m.left()
        m.forward()
        if dir == FORWARD:
            m.forward()
        if dir == RIGHT:
            m.right()
            m.forward()

        
solveDFS()

m.start(5,5)
solve()