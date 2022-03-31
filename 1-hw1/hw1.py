
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
    #(n*1)+(n*1) -> O(n)
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
# Running Time: 
############################################################################

def reverse(l):
    """
    >>> l = [1, 2, 3, 4, 5]
    >>> reverse(l)
    [5, 4, 3, 2, 1]
    >>> l
    [5, 4, 3, 2, 1]
    """
    pass

############################################################################
#
# Problem 3
# Compute the transpose of a matrix in place.
#
# What is the input size measuring?
# Running Time: 
############################################################################

def transpose(m):
    """
    >>> m = [[1,2,3],[4,5,6],[7,8,9]]
    >>> transpose(m)
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    >>> m
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    """
    pass

############################################################################
#
# Problem 4
# Given a list of points, return the distance between the two closest points.
# The distance between two points (x1,y1) and (x2,y2) is:
# d = sqrt((x2-x1)^2 + (y2-y1)^2)
#
# Running Time: 
############################################################################

def pointDist(points):
    """
    >>> pointDist([(1,1), (4,5), (13,6)])
    5
    """
    pass

############################################################################
#
# Problem 5
# multiply two matrices A and B.
# For the running time A is an m*n matrix, and B is an n*l matrix.
#
# what is the size of the output? ?*?
# Running Time: 
############################################################################

def matMul(A,B):
    """
    >>> matMul([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]])
    [[58, 64], [139, 154]]
    """
    pass


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
# Running Time: 
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
    pass

############################################################################
#
# Problem 7
# compute the integer square root of x.
# This is the largest number s such that s^2 <= x.
#
# You can assume that arithmetic operations are constant time for this algorithm.
#
# What is the input size?
# Running Time: 
############################################################################

def isqrt(x):
    """
    >>> isqrt(6)
    2
    >>> isqrt(121)
    10
    >>> isqrt(64)
    8
    """
    pass

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
# Running Time: 
############################################################################

def wordSearch(word,grid):
    """
    >>> s = "bats"
    >>> g = ["abrql", "exayi", "postn", "cbkrs"]
    >>> wordSearch(s,g)
    True
    """
    pass

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
# Running Time: 
############################################################################

def convexHull(points):
    """
    >>> convexHull([(1,1), (4,2), (4,5), (7,1)])
    [(1, 1), (4, 5), (7, 1)]
    """
    pass

############################################################################
#
# Problem 10: Running time
#
# Find the Theta time complexity for the following functions.
# If the problem is a summation, give a closed form first.
#
# 1. f(n) = n^2 + 2n + 1
# 2. f(n) = sum(i=0, n, sum(j=0, i, 1) )
# 3. f(n) = (n+1)!
# 4. f(n) = sum(i=0, n, log(i))
# 5. f(n) = log(n!)
############################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
