
# CS 350: Homework 3
# Due: Week of 4/18
# Name: Alex Harris

# for this homework, unless I'm asking you to sort a list,
# you are allowed to use the sorted function in Python.
# sorted takes a list, and returns a sorted copy of the list in Theta(n*log(n)) time.

############################################################################
#
# Problem 1
# Compute the largest gap between two numbers in a list.
#
# for example: gap([1,6,2,4,9]) == 3 because the gap between 6 and 9 is 3.
# The gap isn't 8 because even thought 9-1 is 8, there is a 4 in the middle
# of those numbers.
############################################################################
def gap(l):
    """
    >>> gap([1,6,2,4,9])
    3
    """
    gappiest = 0
    l.sort()
    for i in range(len(l)-1):
        if (l[i+1] - l[i]) > gappiest:
            gappiest = l[i+1] - l[i]
    
    return gappiest
############################################################################
#
# Problem 2
# We can concatenate two numbers together to get a new number.
# for example: 44 concatenated with 55 = 4455
# We can concatenate a list of numbers by concatenating all the numbers.
# concat([1,2,55,3]) = 12553
#
# If we rearrange the list, we can get a different number.
# concat([2,55,1,3]) = 25513
#
# Write a function to find the largest value we can get from concatenating a list.
#
# Running Time: T(n * log(n))
############################################################################
def concatenate(l):
    out = ""
    for x in l:
        out = out + str(x)
    return int(out)

def largestConcat(l):
    """
    >>> largestConcat([1,2,55,3])
    55321
    """
    l.sort(reverse=True)
    
    return concatenate(l)


############################################################################
#
# Problem 3
# Write a function to return the number of unique elements in an array.
# for example the list [3,6,2,3,2,7,4] has 3 unique elements, 6, 7, and 4.
#
# Running Time: 
############################################################################
def numberUnique(l):
    """
    >>> numberUnique([3,6,2,3,2,7,4])
    3
    """
    pass


############################################################################
#
# Problem 4
# Implement insertion sort from class.
#
# Running Time: 
############################################################################
def insertionSort(l):
    # """
    # >>> insertionSort([3,6,2,5,1])
    # [1,2,3,5,6]
    # """
    pass

############################################################################
#
# Problem 5
# Use the heap from last homework to sort an array.
#
# Running Time: 
############################################################################
def heapSort(n):
    # """
    # >>> heapSort([3,6,2,5,1])
    # [1,2,3,5,6]
    # """
    pass


if __name__ == "__main__":        
    import doctest
    doctest.testmod()