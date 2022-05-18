# CS 350: Homework 6
# Due: Week of 6/16
# Name: Alex Harris
    

import math

def machine(data, code):
    i = 0
    value = 0
    for instruction in code:
        if i >= len(data):
            raise Exception("Ran out of numbers")
        if instruction == "ADD":
            value += data[i]
            i += 1
        elif instruction == "MUL":
            value += data[i] * data[i+1]
            i += 2
        else:
            raise Exception("Illegal Instruction: " + instruction)
    if i < len(data):
        raise Exception("has leftover numbers")
    return value

###########################################################################
# Problem 1:
#
# I've constructed a new data processing language that I call addmul.
# It is a very simple language, programs in addmul consist of two instructions.
# ADD take a value from the data stream and adds it to the current total
# MUL takes the next two number from the current data stream, multiplies them 
# together,
# and adds them to the total.
# That's it.
#
# Your job is to take the data stream (just a list of numbers), and determine
# the program that will produce the largest value.
#
# example:
# largetstProgram([2,3,5])
# should return
# ["ADD","MUL"]
# because this will return 17
# where ["MUL","ADD"] will return 11
# and ["ADD","ADD","ADD"] will return 10
#
# You can run your program by calling 
# machine([2,3,4], ["ADD","MULL]) 
# to run your program
#
# you can use
# machine(numbers, largestProgram(numbers))
# to test your algorithm on any list of numbers.
#
# running time: O(n*Data)
###########################################################################

################ Notes from office hours with Steven #######################
# x1, x2, x3
# largestp(x1:x2:xs)
# Iterative
# x1 + bigseq(x2:xs) OR x1x2 + bigseq(xs)
# start with end and contiue
############################################################################
def largestProgram(data):
    """
    >>> largestProgram([2,3,5])
    ['ADD', 'MUL']
    """
    if data is []:
        return
    total = 0
    memo = [] * len(data)
    
    i = len(data)-1
    while i >= 0:
        if i-1 > 0:
            if (data[i] * data[i-1]) >= data[i]:
                memo.append('MUL')
                i -= 2
            else:
                memo.append('ADD')
                i -= 1
        else:
            memo.append('ADD')
            i -= 1
        
    memo.reverse()
    return memo


###########################################################################
# Problem 2
#
# Implemnt the Floyd-Warshal algorithm from class
#
# For example, the adjacency matrix:
#    [ [  0, inf,  -2, inf], 
#      [  4,   0,   3, inf], 
#      [inf, inf,   0,   2], 
#      [inf,  -1, inf,   0] ]
# should give the distance matrix:
#    [ [  0,  -1,  -2,   0], 
#      [  4,   0,   2,   4], 
#      [  5,   1,   0,   2], 
#      [  3,  -1,   1,   0] ]
# 
#
# Running Time: Theta(n^3)
###########################################################################
def floyd(g):
    """
    >>> floyd([[0, math.inf, -2, math.inf],[4, 0, 3, math.inf],[math.inf, math.inf, 0, 2],[math.inf, -1, math.inf, 0]])
    [[0, -1, -2, 0], [4, 0, 2, 4], [5, 1, 0, 2], [3, -1, 1, 0]]
    """
    n = len(g)
    for w in range(n):
        for u in range(n):
            for v in range(n):
                g[u][v] = min(g[u][v], g[u][w] + g[w][v])
                
    return g

###########################################################################
# Problem 3
#
# Congratulations! You know own a factory that cuts rods.
# Customers will pay a certain value for a length of rods
# for example
# rod length:  3  4  5  6   7
# price:       2  3  6  8  11
#
# You just received a rod of length d, 
# Write a function to determine the most efficient way to cut the rod
# to maximize the profit.
# You should return the maximum profit you can make.
#
# Running Time: O(n*d)
############################################################################

################ Notes from office hours with Steven #######################
#store profit into table after recursive call
#identify largest possible cut, do the math on d with that cut, recurse again
#maxval = max(something, rodsrec(ln[i]) + prc[i]) ??? other args in function call
#must be a positive value to cut
############################################################################
def rods(lengths, prices, d):
    """
    >>> rods([3,4,5,6,7], [2,3,6,8,11], 20)
    30
    """
    val = rodsrec(lengths, prices, d)
    return val

def rodsrec(ln, prc, d):
    if d <= 0:
        return 0
    profit = 0
    for i in range(len(ln)):
        profit = max(profit, rodsrec(ln[i+1:], prc[i+1:], d-ln[i]) + prc[i])
        d -= ln[i]
    
    return profit


############################################################################
# Problem 4: Parenthesizing matrices.
#
# This is the same problem as homework 4, problem 3,
# but this time I want you to do it in polynomial time using dynamic programmign.
# 
# If I multiply and m*l matrix A by an l*n matrix B
# That will take O(n*l*m) time to compute.
#
# If I include a n*o matrix C in this product
# Then I have the m*o matrix A*B*C.
# This is perfectly well defined, but I have a choice.
# Do I multiply (A*B)*C (giving a running time of n*l*m + n*m*o)
# or do i multiply A*(B*C) (giving a running time of l*m*o + n*l*o)
#
# Since matrix multiplication is associative, We will get the same answer.
#
# So, given a list of dimensions of matrices
# (for example [(n,l), (l,m), (m,o)])
# compute the fastest running time that we can do matrix multiplication in. 
#
# example [(3,5), (5,4), (4,7)]
# is 3*5*4 + 3*4*7 = 144
# 
# Running time: O(n^2)
############################################################################

################ Notes from office hours with Steven #########################
# Similar substring problem potentially
# iterative matrix solution
# diagnol mathmatical operations
# A = 2x3, B = 3x5, C = 5x4
#    A  B   C
# A  0  30 70
# B  N  0  60
# C  N  N  0
# 
# A*B = 2*3*5 = 30
# B*C = 3*5*4 = 60
# AB*C = 30+(2*5*4) = 70 <-
# A*BC = 60+(2*3*4) = 84
############################################################################
def matrixParens(s):
    """
    >>> matrixParens([(3,5), (5,4), (4,7)])
    120
    """
    # A = 3x5, B = 5x4, C = 4x7
    #    A  B   C
    # A  0  60 120
    # B  N  0  140
    # C  N  N  0
    # 
    # A*B = 3*5*4 = 60
    # B*C = 5*4*7 = 140
    # AB*C = 60+(3*5*4) = 120 <-
    # A*BC = 140+(3*4*7) = 224
    memo = [[0 for x in range(len(s))] for z in range(len(s))]
    memo2 = [] #holds the final matricies used in AB*C or A*BC

    for i in range(len(memo)):
        for j in range(len(memo[i])):
            if i == j:
                memo[i][j] = 0
            else:
                if i+1 < len(s):
                    memo[i][j] = s[i][0] * s[i+1][0] * s[i+1][1]
                    if i+2 < len(s):
                        if [s[i][0]]+[s[i+1][0]]+[s[i+2][0]] not in memo2:
                            memo2 += [[s[i][0]]+[s[i+1][0]]+[s[i+2][0]]]
                            memo2 += [[s[i][0]]+[s[i+1][1]]+[s[i+2][1]]]
                        
            if i == len(memo)-1 and j == len(memo[i])-1:
                memo[0][-1] = min(max(memo[0])+math.prod(memo2[0]), \
                                  max(memo[1])+math.prod(memo2[-1]))
    # bestsolution = 
    return memo[0][-1]



if __name__ == "__main__":
    import doctest
    doctest.testmod()