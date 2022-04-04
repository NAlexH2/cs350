
# CS 350: Homework 2
# Due: Week of 4/11
# Name: 



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
# What data structure did you use?
# Running Time: 
#########################################3

def findSum(l, s):
    """
    >>> findSum([1,3,5], 8)
    (3, 5)
    >>> findSum([1,2,5], 8)
    None
    """
    pass


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
# What data structure did you use?
# Running Time: 
#########################################3

def mode(l):
    """
    >>> mode([1,2,3,3,4,5])
    3
    """
    pass


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
# pushFront Running Time: 
# pushBack Running Time: 
# popFront Running Time: 
# popBack Running Time: 
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
        self.size = 0
        self.body = []
        self.front = 0
        self.back = 0

    # This method isn't mandatory,
    # but I suggest you implement it anyway.
    # It will help to test this method on it's own.
    # Think carefully about what cases you can have with front and back.
    def resize(self):
        pass

    def pushFront(self, x):
        pass
    def pushBack(self, x):
        pass
    def popFront(self):
        pass
    def popBack(self):
        pass

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
# push Running Time: 
# pop Running Time: 
#########################################3

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
        pass

    def push(self, x):
        pass

    def pop(self):
        pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
