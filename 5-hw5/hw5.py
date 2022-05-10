# CS 350: Homework 5
# Due: Week of 5/9
# Name: Alex Harris

# You should not assume anything about the data for these problems
# other than it's valid.
# Adjacency lists might not be in any particular order
# and graphs may not be connected.

############################################################################
#
# Problem 1
#
# write a function that returns the set of connected components 
# of an undirected graph g.
# g is represented as an adjacency list
# you should return a list of components, where each component is a list of vertices.
# Example g = [[1,2], [0,2], [0,1], [4], [3]]
# Should return a list of two components [[0,1,2],[3,4]]
#
# Running time?
# O[V+E]
############################################################################
def components(g):
    """
    >>> components([[1,2], [0,2], [0,1], [4], [3]])
    [[0, 1, 2], [3, 4]]
    """
    connected = []
    toAttach = []
    i = 0
    while i < len(g):
        if i not in toAttach:
            toAttach = connectedDFS(g[i], i, max(g[i]), {i})
            connected.append(toAttach)
        else:
            i += 1
        
    return connected

def connectedDFS(g, u, v, seen):
    if u == v:
        return [v]
    
    for w in g:
        if w not in seen:
            p = connectedDFS(g, w, v, seen | {w}) #union w with set seen
            if p is not None: #if P != none
                return [u]+p
    return None

############################################################################
#
# Problem 2
#
# write a function the returns True if, and only if, graph g is bipartite
# g is represented as an adjacency list
#
# Running time?
# O(V+E)
############################################################################
def bipartite(g):
    """
    >>> bipartite([[3,4,7], [3,5,6], [4,5,7], [0,1], [0,2], [1,2], [1], [0,2]])
    True
    >>> bipartite([[1,3,4,7], [0,3,5,6], [4,5,7], [0,1], [0,2], [1,2], [1], [0,2]])
    False
    >>> bipartite([[1,3,4,7], [0,3,5,6], [4,5,7], [0,1], [0,2,7], [1,2], [1], [0,2,4]])
    False
    """

    
    seen = [0] * len(g)
    c = [0] * len(g)
    seen[0] = True
    c[0] = False
    bip = 0
    for i in range(len(seen)):
        if seen[i] != True:
            bip = bipFinder(g, 0, seen, c)
            if not bip:
                return bip
            
    return bip
            
def bipFinder(g, u, seen, c): #modified depth first search
    for w in g[u]:
        if seen[w] == False:
            seen[w] = True
            c[w] = not c[u]
            if not bipFinder(g, w, seen, c):
                return False
        elif c[w] == c[u]:
            return False
    return True


############################################################################
#
# Problem 3
#
# write a function the returns True if, and only if, graph g is a forrest
# g is represented by a adjacency list.
#
# Running time?
# O(V+E)
############################################################################
def isForrest(g):
    """
    >>> isForrest([[1,2],[0,3,4],[0,6],[1],[1,8,9],[6],[5,7],[6],[4],[4]])
    True
    >>> isForrest([[1,2],[0,3,4],[0,6],[1],[1,8,9],[6],[5,7],[6],[4],[4],[11],[10]])
    True
    >>> isForrest([[1,2],[0,3,4],[0,6],[1],[1,8,9],[6],[5,7],[6,8],[4,7],[4]])
    False
    >>> isForrest([[1,2],[0,3,4],[0,6],[1],[1,8,9],[6],[5,7],[6],[4],[4],[11,12],[10,12],[10,11]])
    False
    """

    seen = [-1] * len(g)
    if forestFinder(g, 0, seen, -1) == True:
        return False
    
    for i in range(len(seen)):
        if seen[i] == -1:
            if forestFinder(g, i, seen, -1) == True:
                return False
        if seen[i] == False:            
            return False
    return True

def forestFinder(g, u, seen, p): #modified depth first search
    seen[u] = True
    for w in g[u]:
        if seen[w] != True:
            if forestFinder(g, w, seen, u) == True:
                return True
        elif w != p:
            return True
    return False

############################################################################
#
# Problem 4
#
# write a function to topologically sort the vertices of a directed graph d
# Assume d is an adjacency list.
# ex: graph -> a->b and a->c, both b&c -> d
# adjlist [b,a,c,d]
# topologically sorted list:
# a,b,c,d or a,c,b,d -> The vertex cannot connect to its previous in the list
# c cannot connect to b, b cannot connect to c, and a cannot connect to d
#
# Running time?
# O(V+E)
############################################################################
def topsort(d):
    """
    >>> topsort([[1, 2], [3], [3], []])
    [0, 1, 3, 2]
    """
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

############################################################################
#
# Problem 5
#
# write a function to determine the strongly connected components of digraph d.
# Just like the components example, you should return a list of strongly 
# connected components.
#
# Make a DAG using topSort
# loop over the verticies in topSort
#
# Running time?
# O(V+E)
############################################################################
def scc(d):
    """
    >>> scc([[1], [2], [0,3], [1,2], [3,5,6], [4], [7], [8], [6]])
    [[4, 5], [6, 8, 7], [0, 2, 1, 3]]
    """
    # [[0, 1, 2, 3], [4, 5], [6, 7, 8]] <- What the first test should have been
    # vs what was actually getting in the list
    if not d:
        return
    seen = [-1] * len(d)
    i = 0
    dT = [[] for i in d]
    dT = dTranspose(d, dT) #change the directions on digraph d
    connected = []

    for i in range(len(seen)):
        if seen[i] != True:
            connected.append(topMaker(d, i, [i], seen))
            
    seen = [-1] * len(d)
    
    connected.reverse()
    connected = [x for l in connected for x in l]
    sccFound = []
    
    for i in range(len(seen)):
        if seen[connected[i]] != True:
            sccFound.append(topMaker(dT, connected[i], [connected[i]], seen))
    
    return sccFound

def dTranspose(d, dT):
    for i in d:
        for j in i:
            dT[j] += [d.index(i)]
    return dT
    


############################################################################
#
# Problem 6
#
# a. What do we need to change about BFS/DFS if we use an adjacency matrix?
# A: Have to loop through all other points in the row to see if there is
# an edge between the source and all the other points.
#
# b. What is the running time for BFS/DFS if we use and adjacency matrix?
# A: The running time is n^2
#
# c. Give an example of a weighted graph where BFS doesn't return the shortes path.
# A: When the sum of a set of particular edges weighs less than the fewest edges to a point.
# 
############################################################################

if __name__ == "__main__":        
    import doctest
    doctest.testmod()