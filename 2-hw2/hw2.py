
# CS 350: Homework 2
# Due: Week of 4/11
# Name: Alex Harris



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
# What data structure did you use? Just the included list
# Running Time: Theta(1) amortized
#########################################3

from itertools import count
from re import I

from numpy import kaiser


def findSum(l, s):
    """
    >>> findSum([1,3,5], 8)
    (3, 5)
    >>> findSum([1,2,5], 8)
    """
    i = 0
    k = 1

    # print(range(len(l)))
    
    while i <= len(l)-1 and k <= len(l)-1:
        if (l[i] + l[k]) == s:
            return (l[i],l[k])
        elif k == len(l)-1 and i != len(l)-1:
            k = 0
            i += 1
        else:
            k += 1
         
    return


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
# What data structure did you use? list
# Running Time: T(n)
#########################################3

def mode(l):
    """
    >>> mode([1,2,3,3,4,5])
    3
    """
    size = 0
    
    for i in range(len(l)):
        if l[i] > size:
            size = l[i]+1
    
    occur = [0] * size
    most = 0
    
    for i in range(len(l)-1):
        val = l[i]
        occur[val] += 1
        
        if occur[val] > most:
            most = occur[val]
    
    return occur.index(most) #index is T(n) 


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
# pushFront Running Time: T(1) amortized
# pushBack Running Time: T(1) amortized
# popFront Running Time: T(1)
# popBack Running Time:  T(1)
# (my function) bodyValidate Running Time: T(1)
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
        biggersize = len(self.body) << 1
        new_body = malloc(biggersize)
        if self.front > 1:
            i = self.front-1 # -1 due to decrimation in "pushfront" if front == 0
        i = self.front
        if self.back < -1:
            k = self.back+1 # +1 due to decrimation in "pushback" if back == 0
        k = self.back
        while i != 0 or k != 0:
            if i > 0:
                new_body[i] = self.body[i]
                i -= 1
            if k < 0:
                new_body[k] = self.body[k]
                k += 1
        self.size = biggersize
        return new_body
        
    def pushFront(self, x):
        if self.front == 0 and self.back == 0:
            self.body = [x]
            self.front += 1
            return

        if self.body_validate():
            self.body = self.resize()
            if self.front != 0:
                self.front += 1
                self.body[self.front] = x
                return
            self.body[self.front] = x
            self.front += 1
            return
        
        self.body[self.front] = x
        self.front += 1

    def pushBack(self, x):
        if self.back == 0 and self.front == 0:
            self.back -= 1
            self.body = [x]
            return
        
        if self.body_validate():
            self.body = self.resize()
            if self.back != 0:
                self.back -= 1
                self.body[self.back] = x
                return
            self.body[self.back] = x
            self.back -= 1

            return
        
        self.body[self.back] = x
        self.back -= 1

    
    def popFront(self):
        togo = 0
        if self.front == 0 and self.back == 0:
            togo = self.body[self.front]
            self.body = []
            return togo
        
        self.front -= 1
        togo = self.body[self.front]  
        self.body[self.front] = None
        return togo

    def popBack(self):
        togo = 0
        if self.back == 0:
            togo = self.body[self.back]
            self.body = []
            return togo
        
        self.back += 1
        togo = self.body[self.front]
        self.body[self.back] = None
        return togo
    
    def body_validate(self):
    #Returns true if the list is full in each array slot
        if (self.size == 0 
        or id(self.body[self.front+1]) == id(self.body[self.back])
        or len(self.body) + self.back == 0 
        or self.front == self.size):
            return True
        
        return False
        

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
# push Running Time: T(log n)
# pop Running Time: T(log n)
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
        self.size = 0
        self.body = []
        

    def push(self, x):
        
        if self.size % 2 == 0:
            seeker = self.size-1
            parent = (seeker-1)//2
        elif self.size % 2 == 1:
            seeker = self.size-1
            parent = (seeker-2)//2
            
        if self.size == 0:
            self.body = [x]
            self.size = len(self.body)
            return
        
        elif x > self.body[parent]:
            self.body.append(x)
            self.size = len(self.body)
            return

        else:
            self.body.append(x)
            self.size = len(self.body)
            if self.size % 2 == 0:
                seeker = self.size-1
                parent = (seeker-1)//2
            elif self.size % 2 == 1:
                seeker = self.size-1
                parent = (seeker-2)//2
            
            while self.body[seeker] < self.body[parent] and seeker != 0:
                self.body[seeker], self.body[parent] = self.body[parent], self.body[seeker]
                self.body[seeker], self.body[parent+1] = self.body[parent+1], self.body[seeker]
                seeker = parent
                if seeker % 2 == 0:
                    parent = (seeker)//2
                elif seeker % 2 == 1:
                    parent = (seeker-1)//2
            return
                
            
            

    def pop(self):
        togo = 0
        if self.size == 0:
            return
        elif self.size == 1:
            togo = self.body[0]
            self.body = []
            self.size = 0
            
        elif self.size > 1:
            end = self.size - 1
            togo = self.body[0]
            self.body[0] = self.body[end]
            i = 0
            child1 = (2*i)+1
            child2 = (2*i)+2
            while (child1 < self.size-1 
                   and child2 < self.size-1
                   and (self.body[i] > self.body[child1] 
                        or self.body[i] > self.body[child2])):
                if self.body[i] > self.body[child1]:
                    self.body[i], self.body[child1] = self.body[child1], self.body[i]
                    i = child1
                elif self.body[i] > self.body[child2]:
                    self.body[i], self.body[child2] = self.body[child2], self.body[i]
                    i = child2
                child1 = (2*i)+1
                child2 = (2*i)+2
            self.body.pop()
            self.size = len(self.body)
            return togo
                

        return togo

if __name__ == "__main__":        
    import doctest
    doctest.testmod()
