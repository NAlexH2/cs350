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
from queue import Empty
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
# Recurrence worst case: T(n) = 2T(n//2)+n
# Recurrence average case: T(n) = 2T(n//2)+n 
# Running time worst case:  O(n log(n))
# Running time average case: Theta(n log(n))
# 
# When does the worst case happen?
############################################################################

def convexHull(l):
    """
    >>> convexHull([(1,1), (4,2), (4,5), (7,1)])
    [(1, 1), (4, 5), (7, 1)]
    """
    if len(l) < 3: #convex hull must have three points
        return
    elif len(l) == 3:
        return l #if it is explicitly 3, then the list itself is a convex hull
    
    l.sort() #pre-sort, this algo already runs in n log(n) so this is fine
    
    largest = len(l)-1 #the last index in the list which should be the largest point
    lower = []
    upper = []
    thehull = []

    lrp = [l[0],l[largest]] #lrp = left and right most points

    for i in range(len(l)):
        if l[i] not in lrp and l[i][1] < lrp[0][1] and l[i][1] < lrp[1][1]:
            lower = lower + [l[i]] #all points below the dividing line
        if l[i] not in lrp and l[i][1] > lrp[0][1] and l[i][1] > lrp[1][1]:
            upper = upper + [l[i]] #all items above the dividing lines
                        
    
    p3lower = [findp3(lower, lrp, (0,0))] #the lowest point below the dividing line
    p3upper = [findp3(upper, lrp, (0,0))] #the highest point above the dividing line.
    # both run in O(n) as they are recursive linear searches seeking farthest point from
    # previously determined upper and lower halfs

    bad1 = [hullMath(p3lower[0][0], p3lower[0][1], lrp[0][0], lrp[0][1], lower)]
    bad2 = [hullMath(p3upper[0][0], p3upper[0][1], lrp[1][0], lrp[1][1], upper)]
    bad1 = list(bad1) + list(bad2)
    for i in range(len(l)):
        if l[i] not in bad1 and not None:
            thehull = thehull + [l[i]]
    
    return thehull;

def hullMath(x1, y1, x2, y2, l):
    if (x2 or y2) == None:
        return
    if len(l) == 0:
        return []
    rejects = ()
    t = ((x1*y2)+(x2*l[0][1])+(l[0][0]+y1))-((x2*y1)+(l[0][0]*y2)+(x1*l[0][1]))
    if t < 0 and (x1,y1) != l[0]:
        rejects = rejects + l[0]
        hullMath(x1, y1, x2, y2, l[1:])
    
    else:
        hullMath(x1, y1, x2, y2, l[1:])
        
    return rejects


def findp3(scope, lrp, far):
    try: #scan the list moving backwards
        scope[1]
    except IndexError:
        try:
            scope[0]
        except IndexError:
            return (None,None)
        return scope[0] #just return far to maintain a starting of 0,0
    
    far = findp3(scope[1:], lrp, far)
    if far is None: return

    if abs(scope[0][0]) >= abs(lrp[0][0]) and abs(scope[0][1]) <= abs(lrp[1][0]):
        if abs(scope[0][1]) > abs(far[1]):
            far = scope[0]
            return far
        else:
            return far



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