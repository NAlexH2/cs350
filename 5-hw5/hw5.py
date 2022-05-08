# CS 350: Homework 5
# Due: Week of 5/9
# Name: Alex Harris

# You should not assume anything about the data for these problems
# other than it's valid.
# Adjacency lists might not be in any particular order
# and graphs may not be connected.
from collections import deque

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
            toAttach = dfs_rec(g[i], i, max(g[i]), {i})
            connected.append(toAttach)
        else:
            i += 1
        
    return connected

def dfs_rec(g, u, v, seen):
    if u == v:
        return [v]
    
    for w in g:
        if w not in seen:
            p = dfs_rec(g, w, v, seen | {w}) #union w with set seen
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
    """
    # >>> bipartite([[1,3,4,7], [0,3,5,6], [4,5,7], [0,1], [0,2], [1,2], [1], [0,2]])
    # False
    # >>> bipartite([[1,3,4,7], [0,3,5,6], [4,5,7], [0,1], [0,2,7], [1,2], [1], [0,2,4]])
    # False
    
    seen = [False for i in range(len(g))]
    c = [0] * len(g)
    seen[0] = True
    c[0] = False
    
    return bipFinder(g, 0, seen, c)
            
def bipFinder(g, u, seen, c):
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
#
############################################################################
# def isForrest(g):
#     """
#     >>> isForrest([[1,2], [3,4], [5,6], [], [], [], []])
#     True
#     >>> isForrest([[1,2], [3,4], [5,4], [], [], []])
#     False
#     """
#     pass

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
#
############################################################################
# def topsort(d):
#     """
#     >>> topsort([[1, 2], [3], [3], []])
#     [0, 1, 2, 3]
#     """
#     pass

############################################################################
#
# Problem 5
#
# write a function to determine the strongly connected components of digraph d.
# Just like the components example, you should return a list of strongly connected components.
#
# Running time?
#
############################################################################
# def scc(d):
#     """
#     >>> scc([[1], [2], [0,3], [1,2], [3,5,6], [4], [7], [8], [6]])
#     [[0, 1, 2, 3], [4, 5], [6, 7, 8]]
#     """
#     pass



############################################################################
#
# Problem 6
#
# a. What do we need to change about BFS/DFS if we use an adjacency matrix?
#
# b. What is the running time for BFS/DFS if we use and adjacency matrix?
#
# c. Give an example of a weighted graph where BFS doesn't return the shortes path.
#
############################################################################

if __name__ == "__main__":        
    import doctest
    doctest.testmod()