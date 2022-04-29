# CS 350: Homework 4
# Due: Week of 4/4
# Name: Alex Harris

############################################################################
# Problem 1: Quicksort
# 
# implement quicksort described in class.
#
# Recurrence worst case: T(n-1) + 1 + n
# Recurrence average case: T(n) = 2T(n/2) + n
# Running time worst case: O(n^2)
# 
# Running time average case: 
# 2T(n/2)+n | a = 2, b = 2, f(n) = n
# k = log|2|(2) = 1
# n^1 = n
# n = f(n)
# Therefore: f(n) E Theta(n^log|b|(a)) then T(n) E Theta(n^log|b|(a) * log|b|(n)) 
# So...
# Theta(n^log|2|(2) * log|2|(2)) = Theta(2^log|2|(n) * 1) = Theta(n * 1) = Theta(n)
# I'll refrein from repeating this in the future. This was to re-explain to my future self. 
#
# When does the worst case happen?
# A: When the list is already sorted
############################################################################

from curses.ascii import RS
from multiprocessing.connection import wait
from tkinter import W
from turtle import right


def quicksort(l):
    """
    >>> quicksort([3,2,6,1,4])
    [1, 2, 3, 4, 6]
    >>> quicksort([5,4,3,2,1])
    [1, 2, 3, 4, 5]
    >>> quicksort([1,2,3,4,5])
    [1, 2, 3, 4, 5]
    >>> quicksort([1])
    [1]
    >>> quicksort([2,1])
    [1, 2]
    >>> quicksort([432,12,12,12,78,21,90])
    [12, 12, 12, 21, 78, 90, 432]
    >>> quicksort([3,3,3,3,3])
    [3, 3, 3, 3, 3]
    >>> quicksort([])
    []
    """
    if len(l) == 0:
        return l
    small = []
    big = []
    found = []
    for i in range(1,len(l)):
        if l[i] < l[0]:
            small.append(l[i])
        else:
            big.append(l[i])
    
    found += quicksort(small)
    found.append(l[0])
    found += quicksort(big)
    return found

############################################################################
# Problem 2: maximum sublist sum
# 
# A sublist is a contiguous piece of a list
# [1,2,1] is a sublist of [4,1,2,1,3]
# but [1,2,3] isn't.
#
# the sum of a list is just adding all of the elements.
#
# compute the maximum sum of any sublist.
# For example:  [-2,1,-3,4,-1,2,1,-5,4]
# the maximum sublist is [4,-1,2,1] with a sum of 6
# 
# Running time: Theta(n^2)
############################################################################
def maxSublist(l):
    """
    >>> maxSublist([-2,1,-3,4,-1,2,1,-5,4])
    [4, -1, 2, 1]
    
    """


    
    # I spent *way* too long on this question in an attempt to find a recursive soltuion that was n log n but
    # I couldn't scrounge one up. This is the best I got unfortunately and am looking forward to seeing the solution
    # because I was very close several times but just missing some form of logic to get it just right.
    
    maxval = 0
    finallist = []
    for i in range(len(l)-1):
        for j in range(i+1,len(l)-1):
            if sum(l[i:j]) > maxval:
                maxval = sum(l[i:j])
                finallist = l[i:j]
                
    return finallist

############################################################################
# Problem 3: Parenthesizing matrices.
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
# Running time: T(n-1)+4 <- Not 100% certain but I suspect pretty close
############################################################################
def matrixParens(sizes):
    """
    >>> matrixParens([(4,7), (7,5), (5,4)])
    220
    >>> matrixParens([(3,5), (5,4), (4,7)])
    144
    >>> matrixParens([(9,4), (4,9), (9,4), (4,9)])
    972
    >>> matrixParens([(9,4), (4,9)])
    324
    """
    
    totalM = 0
    i = 0
    return mCalc(totalM, sizes, i)

#Recursive function
def mCalc(totalM, m, i):
    finalTM = 0 #To be returned
    
    newM = [0,0] #small list to hold our new matrix after the math is complete
    
    if i+1 > len(m)-1: #if i+1 is out of bounds of the list we have nothing left to do
        return totalM
    
    #Total of the current matrix and the next in format of n*l*m in the form nxl lxm
    totalM += m[i][0] * m[i+1][0] * m[i+1][1]
    
    #modify the temp list to hold the next CORRECT matrix size that would be present after the calculation
    #in test three it's 9*4*9, but we only need the first and last values from the matrix (our n and m in this case)
    #so the next matrix size would be 9x9
    newM[0] = m[i][0]
    newM[1] = m[i+1][1]
    m[i+1] = tuple(newM) #in the form of (A*B)*C, then matrix A*B is AB. Therefore the next set is AB*C, then ABC*D, then ABCD*E etc...
    #This is where the size of the matrix changes to then be calculated on the next go.
    
    i += 1 #increment to get to the next matrix in the list, which was modified to be our new size
    finalTM += mCalc(totalM, m, i)#call it, store it...
    return finalTM #send it.



############################################################################
# Problem 4: Convex Hull again!
# 
# Use the Divide and Conquer algorithm described in class to compute
# the convex hull of a set of points.
#
# Recurrence worst case:
# Recurrence average case:
# Running time worst case:
# Running time average case:
# 
# When does the worst case happen?
############################################################################

def convexHull(l):
    """
    >>> convexHull([(1,1), (4,2), (4,5), (7,1)])
    [(1, 1), (4, 5), (7, 1)]
    """
    #this is a test
    pass

############################################################################
# Problem 5: Recurrence relations
# 
# Give a closed form, and big Theta for the following recurrence relations.
# If it's a divide and conquer relation, then you only need to give the Theta.
#
# a. Give the recurrence relation for Karatsuba's algorithm, and solve it.
# 
# b. Give the recurrence relation for Strassen's algorithm, and solve it.
# 
# c.
# T(1) = 1
# T(n) = T(n-1) + n
# 
# d. 
# T(1) = 1
# T(n) = 2T(n-2) + 1
# 
############################################################################



if __name__ == "__main__":        
    import doctest
    doctest.testmod()