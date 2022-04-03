
# CS 350: Homework 1
# Due: Week of 4/4
# Name: 

# This homework is largely review, and to make sure you have a working version of python.

from distutils.command.build_scripts import first_line_re


from attr import NOTHING
import math

############################################################################
#
# Problem 1
# Find the largest two elements in a list.
# Return your answer in a tuple as (largest, secondLargest)
#
# Running Time: O(n)
############################################################################
def largest2(l):
    """
    >>> largest2([1, 2, 3, 4, 5, 6, 7])
    (7, 6)
    >>> largest2([7, 6, 5, 4, 3, 2, 1])
    (7, 6)
    """
    first = 0
    second = 0
    #(n*1)+(n*1) -> O(2n)
    for i in range(len(l)): #O(n)
        if l[i] > first: #O(1)
            first = l[i] #O(1)

    for i in range(len(l)): #O(n)
        if l[i] > second and l[i] is not first: #O(1)
            second = l[i] #O(1)

    caught_nums = (first, second)

    return caught_nums

############################################################################
#
# Problem 2
# Reverse a list in place,
# and returned the reversed list.
#
# Running Time: O(n)
############################################################################

def reverse(l):
    """
    >>> l = [1, 2, 3, 4, 5]
    >>> reverse(l)
    [5, 4, 3, 2, 1]
    >>> l
    [5, 4, 3, 2, 1]
    """
    #n * 1 -> O(n)
    temp = 0#O(1)
    scan = len(l) - 1#O(1)
    scan2 = scan >> 1#O(1)

    for i in range (scan2):#O(n)
       temp = l[scan-i]#O(1)
       l[scan-i] = l[i]#O(1)
       l[i] = temp#O(1)

    return l

############################################################################
#
# Problem 3
# Compute the transpose of a matrix in place.
#
# What is the input size measuring?
# Running Time: O(n^2)
############################################################################

def transpose(m):
    """
    >>> m = [[1,2,3],[4,5,6],[7,8,9]]
    >>> transpose(m)
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    """
    p = [] #O(1)
    for i in range(len(m)):#O(n)
        p.append([0] * len(m))#O(1)

    for i in range (len(m)):#O(n^2)
        for j in range (len(m[i])):#O(n)
            p[j][i] = m[i][j]#O(1)
    
    m = p
    return m

############################################################################
#
# Problem 4
# Given a list of points, return the distance between the two closest points.
# The distance between two points (x1,y1) and (x2,y2) is:
# d = sqrt((x2-x1)^2 + (y2-y1)^2)
#
# Running Time: O(n^2)
############################################################################

def pointDist(points):
    """
    >>> pointDist([(1,1), (4,5), (13,6)])
    5.0
    """

    small = None #O(1)
    for i in range(len(points)):#O(n^2)
        for j in range(len(points)):#O(n)
            if i is not j:#O(1)
                (x1,y1) = points[i]#O(1)
                (x2,y2) = points[j]#O(1)
                if small == None:#O(1)
                    small = math.sqrt((x2-x1)**2 + (y2-y1)**2)#O(1)

                elif small > math.sqrt((x2-x1)**2 + (y2-y1)**2):#O(1)
                    small = math.sqrt((x2-x1)**2 + (y2-y1)**2)#O(1)

    return small

############################################################################
#
# Problem 5
# multiply two matrices A and B.
# For the running time A is an m*n matrix, and B is an n*l matrix.
#
# what is the size of the output? ?*?
# Running Time: O(n^3)
############################################################################

def matMul(A,B):
    """
    >>> matMul([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]])
    [[58, 64], [139, 154]]
    """

    mfinal = []#O(1)
    for i in range (len(A)): #O(n^3)
        row = [] #O(1)
        for j in range (len(B[0])): #O(n^2)
            temp = 0 #O(1)
            for k in range (len(B)): #O(n)
                temp += A[i][k] * B[k][j] #O(1)
            row.append(temp) #O(1)
        mfinal.append(row) #O(1)

    return mfinal


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
# What is the input size?
# Running Time: O(n)
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
    t = 1  #O(1)
    c = 0  #O(1)
    for i in range(x): #O(n)
        if t & x:  #O(1)
           c += 1  #O(1)
           t = t << 1  #O(1)
        else:  #O(1)
            t = t << 1  #O(1)

    return c

############################################################################
#
# Problem 7
# compute the integer square root of x.
# This is the largest number s such that s^2 <= x.
#
# You can assume that arithmetic operations are constant time for this algorithm.
#
# What is the input size?
# Running Time: O(1)
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
    
    return int(math.sqrt(x)) #O(1)

############################################################################
#
# Problem 8: Word Search
#
# determine if string s is any where in the word grid g.
#
# for example s = "bats"
# g = ["abrql",
#      "exayi",
#      "postn",
#      "cbkrs"]
#
# Then s is in the word grid
#     [" b   ",
#      "  a  ",
#      "   t ",
#      "    s"]
#
# what is your input size?
# Running Time: O(n^2)
############################################################################

def wordSearch(word,grid):
    """
    >>> s = "bats"
    >>> g = ["abrql", "exayi", "postn", "cbkrs"]
    >>> wordSearch(s,g)
    True
    """
    matched = "" #O(1)
    for i in range (len(grid)): #O(n^2)
        for j in range (len(grid[0])): #O(n)
           if i < len(word) and word[i] is grid[i][j]: #O(1)
               matched += grid[i][j] #O(1)
    
    print(matched)

    if matched == word: #O(1)
        return True 
        
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
# Running Time: O(n)
############################################################################

def convexHull(points):
    """
    >>> convexHull([(1,1), (4,2), (4,5), (7,1)])
    [(1, 1), (4, 5), (7, 1)]
    """
    actual = []

    for i in range(len(points)): #O(n)
        (x1, y1) = points[i] #O(1)
        if i != len(points)-1: #O(1)
            (x2, y2) = points[i+1] #O(1)
        elif i == len(points)-1: #O(1)
            (x2, y2) = points[0] #O(1)
        a = y2 - y1 #O(1)
        b = x1 - x2 #O(1)
        c = (x1*y2) - (x2*y1) #O(1)
        if c < (a*1+b*1) or c == (a*1+b*1): #O(1)
            actual.append((x1,y1)) #O(1)

    
    return actual

############################################################################
#
# Problem 10: Running time
#
# Find the Theta time complexity for the following functions.
# If the problem is a summation, give a closed form first.
#
# 1. f(n) = n^2 + 2n + 1
#   Quadratic Time
#
# 2. f(n) = sum(i=0, n, sum(j=0, i, 1) )
#   Quadratic Time
#
# 3. f(n) = (n+1)!
#   Factorial Time

# 4. f(n) = sum(i=1, n, log(i))
#   Logarithmic Time
#
# 5. f(n) = log(n!)
#   n log n - Linearithmic from textbook
############################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
