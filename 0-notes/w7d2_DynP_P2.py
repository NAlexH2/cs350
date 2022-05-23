# Today was again just more coding problems discussed in class.
import math

def test(g):
    """
    >>> test(1)
    1
    """
    return g

#min path using dynamic programming using
#bottom up approach
def minpath(dag, u, v):
    """
    >>> dag = [[(1,3),(2,1)],[(3,2)],[(3,2)],[]]
    >>> minpath(dag, 0, 3)
    """
    d = [math.inf] * len(dag)
    d[u] = 0
    for s in topsort(dag):
        for (t,w) in dag[s]:
            d[t] = min(d[s] + w, d[t])
    
    #Returning the final item in the memo
    #Which should also be the final item in the dag
    return d[v]

#######End example


#####Warshall Algo
def warshall(adj):
    T = adj
    for w in range(len(adj)):
        for u in range(len(adj)):
            for v in range(len(adj)):
                if T[u][w] == 1 and T[w][v] == 1:
                    T[u][v] = 1

    return T


###Shortest possible path changem-up version:
def warshall2(g):
    n = len(g)
    for w in range(n):
        for u in range(n):
            for v in range(n):
                g[u][v] = min(g[u][v], g[u][w] + g[w][v])
                
    return g
#######End example




####Floyd-Warshall algo example
#changing possible paths in a adj. matrix IF there is actually a path
#from u to v
def floyd_warshall(g):
    '''i have no idea what to put for a test case here...'''
    n = len(g)
    for w in range(n):
        for u in range(n):
            for v in range(n):
                #left hand = itself OR bitwise and operation
                g[u][v] = g[u][v] | (g[u][w] & g[w][v])
    return g 

########End example


#####Longest Common Substring
###Looking at two strings, the longest possible string compared against the two
#O(s * t)
def LCS(s,t):
    '''What even is testing?'''
    T = [[0]* (range(len(t))) for i in s]
    largest = 0
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                if i == 0 or j == 0:
                    T[i][j] = 1
                else:
                    T[i][j] = T[i-1][j-1] + 1
                largest = max(largest, T[i][j])
    return largest

    
####Subset Sum
##Find sum subset of ints that add up to target T
def subsetSum(xs, i):
    '''Didn't have time for this one'''
    pass
###End example






######Code pulled from assignment 4
#Works mostly I think?
def topsort(d):
    seen = [-1] * len(d)
    sT = []
    for i in range(len(seen)):
        if seen[i] != True:
            sT = topMaker(d, 0, [0], seen)
    return sT

def topMaker(d, u, sT, seen):
    seen[u] = True
    for w in d[u]:
        if seen[w] != True:
            sT.append(w)
            topMaker(d, w, sT, seen)
            
    return sT



if __name__ == "__main__":        
    import doctest
    doctest.testmod()