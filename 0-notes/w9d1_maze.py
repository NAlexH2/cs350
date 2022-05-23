import random as rng
import turtle as t

SOUTH  = 0
EAST   = 1
NORTH  = 2
WEST   = 3

class maze(object):
    def __init__(self,r,c):
        self.rows = r
        self.cols = c
        #walls[dir][row][col] where dir is 0 (down) 1 (right)
        self.walls = [[[False for d in [SOUTH,EAST]] \
                              for j in range(c)]   \
                              for i in range(r)]
        self.gen()
        self.draw()
        self.dir = EAST
        self.row = 0
        self.col = 0
        self.valid = True

    def gen(self):
        seen = [[False for j in range(self.cols)] \
                       for i in range(self.rows)]
        self.gen_maze(seen, 0, 0)

    def gen_maze(self, seen, r, c):
        seen[r][c] = True;

        # shuffel the directions, so we actually go in a random direction
        #        NORTH           WEST          SOUTH        EAST
        order = [(-1,0,SOUTH), (0,-1,EAST), (0,0,SOUTH), (0,0,EAST)]
        rng.shuffle(order)

        # for each possible direction check if we can go there
        # we use order to randomly permute the directions.
        for (dr,dc,d) in order:

            nr = r + (d == SOUTH)  * (2*dr + 1)
            nc = c + (d == EAST) * (2*dc + 1)

            # if we are within the bounds of our maze
            # AND we haven't visited the square above us yet.
            if 0 <= nr < self.rows and \
               0 <= nc < self.cols and \
               not seen[nr][nc]:
                # kill the wall between this square and the square above us
                self.walls[r+dr][c+dc][d] = True

                # continue from the square above us.
                self.gen_maze(seen, nr, nc);
            # end if
        # end for
    # end gen_maze

    def draw(self):
        #setup
        col = 400/self.cols
        row = 400/self.rows
        t.ht()
        t.speed("fastest")
        t.penup()
        t.goto(-200,200)

        # draw boarder
        t.pendown()
        t.forward(400)
        t.backward(400)
        t.right(90)
        t.forward(400)
        t.backward(400)

        #draw vertical lines
        for c in range(self.cols):
            t.penup()
            t.goto((c+1)*col - 200, 200)
            for r in range(self.rows):
                if self.walls[r][c][EAST]:
                    t.penup()
                else:
                    t.pendown()
                t.forward(row)
        t.left(90)

        #draw horizontal lines
        for r in range(self.rows):
            t.penup()
            t.goto(-200, 200 - (r+1)*row)
            for c in range(self.cols):
                if self.walls[r][c][SOUTH]:
                    t.penup()
                else:
                    t.pendown()
                t.forward(row)

        #put us at the start facing right
        t.penup()
        t.goto(-200+col/2,200-row/2)
        t.st()
        t.speed("normal")
        t.color("blue")
        t.pendown()

    def down(self):
        return self.row < self.rows and self.walls[self.row][self.col][SOUTH]

    def right(self):
        return self.col < self.cols and self.walls[self.row][self.col][EAST]

    def up(self):
        return self.row > 0 and self.walls[self.row-1][self.col][SOUTH]

    def left(self):
        return self.col > 0 and self.walls[self.row][self.col-1][EAST]

theMaze = None

def start(rows, cols):
    global theMaze
    theMaze = maze(rows,cols)

def canGoLeft():
    return theMaze.dir == SOUTH and theMaze.right() or \
           theMaze.dir == EAST  and theMaze.up() or \
           theMaze.dir == NORTH and theMaze.left() or \
           theMaze.dir == WEST  and theMaze.down()

def canGoForward():
    return theMaze.dir == SOUTH and theMaze.down() or \
           theMaze.dir == EAST  and theMaze.right() or \
           theMaze.dir == NORTH and theMaze.up() or \
           theMaze.dir == WEST  and theMaze.left()

def canGoRight():
    return theMaze.dir == SOUTH  and theMaze.left() or \
           theMaze.dir == EAST   and theMaze.down() or \
           theMaze.dir == NORTH  and theMaze.right() or \
           theMaze.dir == WEST   and theMaze.up()

def canGo(square, dir):
    (row,col) = square
    if dir == SOUTH:
        return row < theMaze.rows and theMaze.walls[row][col][SOUTH]
    if dir == EAST:
        return col < theMaze.cols and theMaze.walls[row][col][EAST]
    if dir == NORTH:
        return row > 0 and theMaze.walls[row-1][col][SOUTH]
    if dir == WEST:
        return col > 0 and theMaze.walls[row][col-1][EAST]


def forward():
    if not canGoForward():
        theMaze.valid = False
        t.color("red")
    if theMaze.dir == SOUTH:
        t.forward(400/theMaze.rows)
        theMaze.row += 1
    if theMaze.dir == EAST:
        t.forward(400/theMaze.cols)
        theMaze.col += 1
    if theMaze.dir == NORTH:
        t.forward(400/theMaze.rows)
        theMaze.row -= 1
    if theMaze.dir == WEST:
        t.forward(400/theMaze.cols)
        theMaze.col -= 1


def right():
    theMaze.dir = (theMaze.dir + 3) % 4
    t.right(90)

def left():
    theMaze.dir = (theMaze.dir + 1) % 4
    t.left(90)

def finished():
    return theMaze.row == theMaze.rows - 1 and \
           theMaze.col == theMaze.cols - 1

def finish(square):
    (row,col) = square
    return row == theMaze.rows - 1 and \
           col == theMaze.cols - 1
