"""
Day 1 notes

Analysis of Algos
- Use big O notation to measure the running time

<<<<<<< HEAD
* How to measure the algo?
=======
* How to measure the algo?1
>>>>>>> First commit
- Measure input in repsct to the input size
- Measure the operations, not the running time

* What is the input size?
- for lists it's the number of elements
- for matricies it's the total number of elements
    - if M is m x n, this it's size is m * n
    - if M is a n x m matrix, then we sometime measure it as O(f(n))
        ***THIS IS WRONG***
- for graphs, we measure by number of verticies and edges seperately

* What are operations?
- Not defined
- Pick what is convenient for an operation
- For sorting we usually pick number of comparisons
- For numeric usually pick arithmetic or bitwise operations
"""

l = [99, 44, 100, 4, 12039]
def minElem(l):
    l.sort()
    print(f"{l[0]}")
    return l[0]
    #runtime: O(n) or O(1)

"""
soln:
def minElem(l):
    minEl = l[0]
    for i in range(len(l)):
        if minEl < l[i]:
            minEl = l[i]
    return minEl
"""

# Didn't finish this one (STRING MATCHING)
s = "bat"
text = "Can you find me some batteries"
def match(s, text):
    for i in range(len(text)):
        if text.lower() is b:
            print("Indeed")
            return True
    print("Indeednt")
    return False


"""
String Matching
- This is a little harder, but gives us our first algo technique
- This is the sliding window technique
- We look at a window in 'text' and see if it matches 's'.

soln:
def match(s, text):
    for i in range(len(text) - len(s))
    matches = True
    j = 0
    # check if s matches the window
    while j < len(s) and matches:
        matches = s[j] == test[i + j]
        j += 1
        if matches:
            return True
    return False

runtime: (n-k)*k
O(n^2)
"""

x = 44
def ilog(x):
    for i in range(1,x):
        if 2**i > x:
            return i-1
    return None
"""
Could also do bitshifting right instead of divide by 2 to come down to O(n) instead of O(n^2)
"""


if __name__ == "__main__":
    #import doctest
    #doctest.testmod()
    #how to use this properly? Refer to day 1 lecture notes (maybe >>> was missing/required)
    minElem(l)
    match(s, text)
    ilog(x)
