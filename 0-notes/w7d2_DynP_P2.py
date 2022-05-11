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

#####Warshall algo example
#changing possible paths in a adj. matrix IF there is actually a path
#from u to v
def warshall(g):
    '''i have no idea what to put for a test case here...'''
    n = len(g)
    for w in range(n):
        for u in range(n):
            for v in range(n):
                #left hand = itself OR bitwise and operation
                g[u][v] = g[u][v] | (g[u][w] & g[w][v])
    return g 

########End example









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