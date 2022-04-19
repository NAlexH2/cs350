
# CS 350: Homework 2
# Solutions



#########################################3
# Problem 1:
#
# Find a pair with a given sum.
#
# input: a list of integers l, an integer s
# return None if this sum doesn't exist in the array.
# output: a pair of numbers (a,b) where a,b are in l, and a + b == s
# findSum([1,3,5], 8) returns (3, 5)
# 
# What data structure did you use? set
# Running Time: Theta(n) since set has Theta(1) lookup time.
#########################################3

def findSum(l, s):
    """
    >>> findSum([1,3,5], 8)
    (3, 5)
    >>> findSum([1,2,5], 8)
    """
    # we can make a set of all of the numbers s - l[i]
    # if l[j] is in this set, then l[i] + l[j] = s.
    diff = set()
    for i in range(len(l)):
        diff.add(s - l[i])
    # end for

    for j in l:
        if j in diff:
            return (j, s-j)
        # end if
    # end for

    return None

#########################################3
# Problem 2:
#
# Find the mode of a list of numbers.
# The mode of a list is the most commonly occurring number in the list.
#
# input: a list of integers l
# output: the mode of l.
# mode([1,2,3,3,4,5]) returns 3
# 
# What data structure did you use? dictionary
# Running Time: Theta(n)
#########################################3

def mode(l):
    """
    >>> mode([1,2,3,3,4,5])
    3
    """
    # we just make a dictionary to count the numbers.
    d = {}
    for x in l: #O(n)
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
        # end if
    # end for

    # find the number with the highest count.
    # It's at least as big as the first number in the list.
    modeI = l[0]
    for k in d: #O(n) since there are no more and n entries in d
        if d[k] > d[modeI]:
            modeI = k
        # end if
    # end for

    return modeI


#########################################3
# Problem 3:
#
# We talked about a ring buffer in class
# A ring buffer has four methods
# pushFront(x)
# pushBack(x)
# popFront()
# popBack()
#
# Your job is to implement these four methods.
# We can't just use the list append method to resize the ring buffer.
# we might have front and back in the middle of the buffer,
# and append only adds new space at the end.
# for that reason, you're going to have to copy
# the array over to a bigger one manually.
#
# I've provided a malloc function to allocate a new array.
# You need to copy the old array into the new one
# but be sure to keep elements in the correct position
#
# For example if we have the buffer :
#
#     v back
# [3, 4, 1, 2]
#        ^ front
#
# and we were to resize it, then the new buffer should be
#     v back
# [3, 4, None, None, None, None, 1, 2]
#                                ^ front
#    
# pushFront Running Time: Theta(1) amortized time (because of resize)
# pushBack Running Time:  Theta(1) amortized time (because of resize)
# popFront Running Time:  Theta(1)
# popBack Running Time:   Theta(1)
#########################################3

def malloc(size):
    return [None] * size

class RingBuffer():
    """
    >>> r = RingBuffer()
    >>> r.pushBack(3)
    >>> r.pushBack(4)
    >>> r.pushBack(5)
    >>> r.pushFront(2)
    >>> r.pushFront(1)
    >>> r.popFront()
    1
    >>> r.popFront()
    2
    >>> r.popFront()
    3
    >>> r.popFront()
    4
    >>> r.popFront()
    5
    """

    def __init__(self):
        self.body = malloc(4)
        self.front = 0
        self.back = 0
        self.size = 0

    # helper functions to move the the next and previous indices
    # while still wrapping around the queue
    def next(self, i):
        return (i+1) % len(self.body)
    def prev(self, i):
        return (i-1 + len(self.body)) % len(self.body)

    # We want to copy everything to the new array
    # but if this happens, then front must have ran into back.
    # so we have and array of 
    # [ ... x ...]
    #      ^ ^
    #   back front
    # everything before back will stay in place
    # everything after front will move to the end
    # and we pad out the middle.
    # since + takes Theta(n) time for lists, this still runs in Theta(n).
    def resize(self):
        self.body = self.body[:self.back] + malloc(self.size) + self.body[self.front:]
        self.front += self.size 

    def pushFront(self, x):
        if self.size == len(self.body):
            self.resize()
        self.front = self.prev(self.front)
        self.body[self.front] = x
        self.size += 1

    def pushBack(self, x):
        if self.size == len(self.body):
            self.resize()
        self.body[self.back] = x
        self.back = self.next(self.back)
        self.size += 1

    def popFront(self):
        x = self.body[self.front]
        self.front = self.next(self.front)
        self.size -= 1
        return x

    def popBack(self):
        x = self.body[self.prev(self.back)]
        self.back = self.prev(self.back)
        self.size -= 1
        return x

#########################################3
# Problem 4:
#
# We talked about a heap in class
# A heap is a data structure that has a constructor,
# a push method, and a pop method.
# Your job is to implement these methods in Python.
# I've given you the skeleton for the class,
# you need to fill it in.
# 
# 
# push Running Time: Theta(log(n))
# pop Running Time:  Theta(log(n))
#########################################3


# these are just helper functions for readability
# left returns the index of the left child
# right returns the index of the right child
# up returns the index of the parent
def left(i):
    return 2*i+1
def right(i):
    return 2*i+2
def up(i):
    return (i-1)//2



class Heap():
    """
    >>> h = Heap()
    >>> h.push(3)
    >>> h.push(2)
    >>> h.push(4)
    >>> h.push(1)
    >>> h.push(5)
    >>> h.pop()
    1
    >>> h.pop()
    2
    >>> h.pop()
    3
    >>> h.pop()
    4
    >>> h.pop()
    5
    """
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
