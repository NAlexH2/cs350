
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
    if not l:
        return
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
# Running Time: Theta(n * log(n))
############################################################################
def concatenate(l): #TODO - Make the array a string and make it work that way
    out = ""
    for x in l:
        out = out + str(x)
    return int(out)

def largestConcat(l):
    """
    >>> largestConcat([1,2,55,3])
    55321
    >>> largestConcat([97,976,8])
    979768
    >>> largestConcat([87, 879, 5])
    879875
    """
    if not l:
        return
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
    # If the list is empty
    if not l:
        return

    # Using a similar trick from assignment 2 on finding the mode, but for finding
    # duplicates. First we need to make a list the largest value in the list + 1 
    # to account for all numbers 0->max(l)
    l.sort(reverse=True)
    nodupes = [0] * (l[0]+1)
    
    # Empty list of the unique numbers to be found
    uniquenums = 0
    

    for i in range(len(l)):
        nodupes[l[i]] += 1
        
        # If we're 1, great lets just do that now
        # and correct later
        if nodupes[l[i]] == 1:
            uniquenums += 1
            
        # We've been here before, and now we're larger than 1
        # so lets just undo our counting
        elif nodupes[l[i]] > 1:
            uniquenums -= 1

    return uniquenums


############################################################################
#
# Problem 4
# Implement insertion sort from class.
#
# Running Time: Theta(n^2)
############################################################################
def insert(l,x):
    l.append(x)
    i = len(l)-1
    while l[i] < l[i-1]:
        l[i], l[i-1] = l[i-1], l[i]
        i -= 1
    
    return l
        
def insertionSort(l): #TODO - FIX THIS
    """
    >>> insertionSort([3,6,2,5,1])
    [1, 2, 3, 5, 6]
    """
    if not l:
        return
    
    l2 = []
    for i in range(len(l)-1,-1,-1):
       insert(l2, l[i])
    
    return l2

############################################################################
#
# Problem 5
# Use the heap from last homework to sort an array.
#
# Running Time: 
############################################################################
def heapSort(n):
    """
    >>> heapSort([3,6,2,5,1])
    [1, 2, 3, 5, 6]
    """
    h = Heap()
    l2 = []
    while n or h.body:
        if n:
            h.push(n.pop())
        else:
            l2.append(h.pop())
    return l2



###
# Steven's code solutions from assignment two we've been given permission to use
# for this question.
###
def left(i):
    return 2*i+1
def right(i):
    return 2*i+2
def up(i):
    return (i-1)//2

class Heap():

    def __init__(self):
        self.body = []

    def push(self, x):
        self.body.append(x)
        i = len(self.body)-1

        # while the current node i is less than the parent node, swap them
        while up(i) >= 0 and self.body[up(i)] > self.body[i]:
            self.body[i], self.body[up(i)] = self.body[up(i)], self.body[i]
            i = up(i)
        # end while

    def pop(self):
        out = self.body[0]
        self.body[0] = self.body[-1]
        self.body.pop()
        i = 0
        # While the current node i is less then one of the children, swap it with the smaller one.
        while right(i) < len(self.body) and self.body[i] > min(self.body[left(i)], self.body[right(i)]):

            # the left child is smaller
            if self.body[left(i)] < self.body[right(i)]:
                self.body[i], self.body[left(i)] = self.body[left(i)], self.body[i]
                i = left(i)

            # the right child is smaller
            else:
                self.body[i], self.body[right(i)] = self.body[right(i)], self.body[i]
                i = right(i)
            #end if

        #end while
    
        # It's possible that we only have a left child, so make sure to swap
        # with that if we're bigger.
        if left(i) < len(self.body) and self.body[i] > self.body[left(i)]:
            self.body[i], self.body[left(i)] = self.body[left(i)], self.body[i]
        #end if

        return out
    

if __name__ == "__main__":        
    import doctest
    doctest.testmod()