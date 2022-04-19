
import math

# CS 350: Homework 1
# Due: Week of 4/4
# Name: 

# This homework is largely review, and to make sure you have a working version of python.

############################################################################
#
# Problem 1
# Find the largest two elements in a list.
# Return your answer in a tuple as (largest, secondLargest)
#
# Running Time: O(n)
# our operations are comparisons
# we loop n-2 times,
# and each loop we do up to two comparisons
# so we have (n-2)*2 = 2n-4 comparisons
# even thought we're making a copy of n[2:], that's still a factor of n.
############################################################################
def largest2(l):
    """
    >>> largest2([1, 2, 3, 4, 5, 6, 7])
    (7, 6)
    >>> largest2([7, 6, 5, 4, 3, 2, 1])
    (7, 6)
    >>> largest2([5, 2, 6, 4, 3, 7, 1])
    (7, 6)
    >>> largest2([5, 2, 7, 4, 3, 6, 1])
    (7, 6)
    """
    big = max(l[0],l[1])
    small = min(l[0],l[1])
    for x in l[2:]:
        if x > big:
            (big,small) = (x,big)
        elif x > small:
            small = x
        # end if
    # end for
    return (big,small)
        


############################################################################
#
# Problem 2
# Reverse a list in place,
# and returned the reversed list.
#
# Running Time: O(n)
# The operation here is assignment
# we loop n/2 times, and we swap two elements each iteration.
############################################################################

def reverse(l):
    """
    >>> l = [1, 2, 3, 4, 5]
    >>> reverse(l)
    [5, 4, 3, 2, 1]
    >>> l
    [5, 4, 3, 2, 1]
    """
    for i in range(len(l)//2):
        (l[i],l[-1-i]) = (l[-1-i],l[i])
    # end for
    return l

############################################################################
#
# Problem 3
# Compute the transpose of a matrix.
#
# What is the input size measuring? The input size is n = r*c 
# where r is the number of rows, and c is the number of columns
# Running Time: O(n)
# We assign each of the n elements in the matrix to the transpose
############################################################################

def transpose(m):
    """
    >>> m = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    >>> transpose(m)
    [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]
    """
    # we can build the transpose row by row.
    mT = []
    for c in range(len(m[0])):
        mT.append([])
        for r in range(len(m)):
            mT[c].append(m[r][c])
        # end for r
    # end for c

    # other possibility: we build the entire matrix, and set the elements
    # mT = [[0] * len(m[0]) for x in m ]
    # for c in range(len(m[0])):
    #     for r in range(len(m)):
    #         mT[c][r] = m[r][c]
    #     # end for r
    # # end for c
    return mT 

############################################################################
#
# Problem 4
# Given a list of points, return the distance between the two closest points.
# The distance between two points (x1,y1) and (x2,y2) is:
# d = sqrt((x2-x1)^2 + (y2-y1)^2)
#
# Running Time: O(n^2)
############################################################################

def dist(p1,p2):
    (x1,y1) = p1
    (x2,y2) = p2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def pointDist(points):
    """
    >>> pointDist([(1,1), (4,5), (13,6)])
    5.0
    """
    minDist = dist(points[0], points[1])
    for p1 in points:
        for p2 in points:
            if p1 != p2:
                minDist = min(dist(p1,p2), minDist)
            # end if
        # end for p2
    # end for p1
    return minDist

############################################################################
#
# Problem 5
# multiply two matrices A and B.
# For the running time A is an m*n matrix, and B is an n*l matrix.
#
# what is the size of the output? m*l
# Running Time: O(m*n*l), for square matrices it's O(n^3).
############################################################################

def matMul(A,B):
    """
    >>> matMul([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]])
    [[58, 64], [139, 154]]
    """
    m = len(A)
    n = len(A[0])
    l = len(B[0])

    # another way to make a matrix
    # We can use a list comprehension
    # [0] * l is a row of l zeros
    # [[0] * l for row in A] means, make a list of l zeros for each row in A
    # in general [exp for elem in list] mean make a list of exp for every elem in list.
    # usually exp will use elem in some way, but it doesn't have to.
    # example: [x**2 for x in [1,2,3,4]] will square all the numbers in the list
    # giving us [1,4,9,16]
    # This still takes O(m*l) time 
    C = [[0] * l for row in A]

    for i in range(m):
        for j in range(l):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
            # end for k
        # end for j
    # end for i
    return C


############################################################################
#
# Problem 6
# Compute the number of 1s that would be in the binary representation of x
# for example: 30 = 11110 in base 2, and it has 4 1s.
#
# For full credit, you should assume that 
# arithmetic operations are *not* constant time.
# bitwise operations are constant time though.
#
# What is the input size? n = log(x)
# Running Time: n*log(n)
############################################################################

def popcount(x):
    """
    >>> popcount(7)
    3
    >>> popcount(30)
    4
    >>> popcount(256)
    1
    """
    count = 0

    # analysis here is tricky, because
    # adding 1 here could potentially flip all of the bits in count
    # but count can never be bigger than log(x) = n
    # so, in the worst case this takes 
    # log(1) + log(2) + ... log(n) = n*log(n) time
    # In reality, this actually take O(n) time, 
    # but we'll get to that with amortized analysis.
    while x != 0:
        if x&1 == 1:
            count += 1
        x = x >> 1 #O(1)
    # end while

    return count

############################################################################
#
# Problem 7
# compute the integer square root of x.
# This is the largest number s such that s^2 <= x.
#
# You can assume that arithmetic operations are constant time for this algorithm.
#
# What is the input size? n = log(x)
# Running Time: O(2^(n/2))
# since it's sqrt(x) = x^1/2 = (2^n)^(1/2) = 2^(n/2)
############################################################################

def isqrt(x):
    """
    >>> isqrt(6)
    2
    >>> isqrt(121)
    11
    >>> isqrt(64)
    8
    """
    sqrtx = 1
    while sqrtx * sqrtx <= x:
        sqrtx += 1
    return sqrtx - 1

############################################################################
#
# Problem 8: Word Search
#
# determine if string s is any where in the word grid g.
#
# for example s = "bats"
# g = ["abrql",
#      "exabi",
#      "postn",
#      "cbkrs"]
#
# Then s is in the word grid
#     [" b   ",
#      "  a  ",
#      "   t ",
#      "    s"]
#
# what is your input size? n = g^2 + g
# Let's say that the grid is a g*g matrix, and the word has size s
# in the worst case our word can be as long as a row in the grid.
# Therefore in the worst case our input is g^2 + g.
#
# Running Time: O(g^3) = O(n^(3/2)) since g ~= sqrt(n)
############################################################################

# check if the word is at position i,j going in direction di,dj
# (di,dj) is the direction of word we're checking
# (-1,-1) (-1,0) (-1,1)
# (0,-1)  (0,0)  (0,1)
# (1,-1)  (1,0)  (1,1)
def checkDir(word,grid,i,j,di,dj): #O(g)
    n = len(word)
    # does the word go off the edge of the grid?
    if 0 <= i + n*di <= len(grid) and \
       0 <= j + n*dj <= len(grid[0]):
        foundWord = True
        for k in range(n): #O(g)
            foundWord = foundWord and grid[i+k*di][j+k*dj] == word[k]
        return foundWord
    return False
                    

# check if the word is at position i,j in the grid
def checkWord(word,grid,i,j): #O(g)

    if grid[i][j] != word[0]:
        return False

    for di in [-1,0,1]: #O(9*g)
        for dj in [-1,0,1]: #O(3*g)
            # We don't check (0,0) because it doesn't go anywhere
            if (di,dj) != (0,0): #O(g)
                if checkDir(word,grid,i,j,di,dj):
                    return True
                # if checkDir
            #if not 0
        # for dj
    # for di
    return False

def wordSearch(word,grid):
    """
    >>> s = "bats"
    >>> g = ["abrql", "exabi", "postn", "cbkrs"]
    >>> wordSearch(s,g)
    True
    """
    m = len(grid)
    n = len(grid[0])
    for i in range(m): #O(g^3)
        for j in range(n): #O(g^2)
            if checkWord(word,grid,i,j): #O(g)
                return True
            #end if
        #end for j
    #end for i
    return False

############################################################################
#
# Problem 9: Convex Hull
#
# In class we learned about the convex hull problem.
# We also learned that for any line segment on the convex hull,
# every other point will we on the same side of that line.
#
# Use this fact to write an algorithm to find all of the points in the convex hull.
#
# for example: [(1,1), (4,2), (4,5), (7,1)] are the points shown below
#
#    *
#
#    *
# *     *
#
# The convex hull is [(1,1), (4,5), (7,1)]
#    *
#   / \
#  /   \
# *-----*
#
# Running Time: O(n^3)
############################################################################

def convexHull(points):
    """
    >>> convexHull([(1,1), (4,2), (4,5), (7,1)])
    [(1, 1), (4, 5), (7, 1)]
    """
    hull = []
    for p1 in points: # O(n^3)
        for p2 in points: # O(n^2)
            (x1,y1) = p1
            (x2,y2) = p2
            
            # the two points have to be different to form a line.
            if p1 != p2: #O(3*n)
                a = y2 - y1
                b = x1 - x2
                c = x1*y2 - x2*y1
                left = False
                right = False
                for p in points: #O(n)
                    (x,y) = p
                    if p not in [p1,p2]:
                        left  = left  or a*x + b*y > c
                        right = right or a*x + b*y < c
                # end for p

                # all points are on the same side,
                # add them to the hull if we haven't seen them.
                if not (left and right): #O(n)
                    if p1 not in hull: #O(n)
                        hull.append(p1)
                    if p2 not in hull: #O(n)
                        hull.append(p2)
                #end if
            # end if
        # end for p2
    # end for p1
    return hull

############################################################################
#
# Problem 10: Running time
#
# Find the Theta time complexity for the following functions.
# If the problem is a summation, give a closed form first.
#
# 1. f(n) = n^2 + 2n + 1 
# O(n^2)

# 2. f(n) = sum(i=0, n, sum(j=0, i, 1) )
# sum(j=0, i, 1) = i
# sum(i=0, n, i) = n(n+1)/2 which is in O(n^2)

# 3. f(n) = (n+1)!
# (n+1)! = (n+1)*n! = n*n! + 1*n!
# O(n*n!)

# 4. f(n) = sum(i=1, n, log(i))
# this is log(n!), but it's in O(n*log(n))
# To see this, notice that 
# sum(i=1,n, log(i)) = 
# log(1) + log(2) + log(3) ... log(n) which is less than 
# log(n) + log(n) + log(n) ... log(n) =
# n*log(n)
# It's actually Theta(n*log(n))
# we can see this becausel 
# log(1) + log(2) + log(3) ... log(n) is bigger than
# log(n/2) + log(n/2 + 1) + ... log(n) which is bigger than
# log(n/2) + log(n/2) + ... log(n/2) =
# n/2*log(n/2) =
# 1/2*n*log(n) - 1/2*n*log(2) >
# 1/2*n*log(n)
#
#
# 5. f(n) = log(n!)
# log(1*2 ... n) = log(1) + log(2) + ... log(n) = sum(i=1,n,log(i))
# so it's in O(n*log(n))
############################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
