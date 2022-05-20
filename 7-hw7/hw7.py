# CS 350: Homework 7
# Due: Week of 5/23
# Name: Alex Harris


################################################################
# Problem 1
# 
# We're going to take the job scheduling problem from class,
# but this time, I want to make sure every job is scheduled.
# If I have a set of n jobs where each job is represented
# by a tuple (s,f),
# Give a greedy algorithm to schdule the jobs on the fewest
# number of processors total
#
# Running Time: Theta(n^2)
#
################################################################

from numpy import sort


def schedule(jobs):
    """
    >>> schedule([(5,40), (30,35), (6,20), (19, 31), (23, 29), (28, 32)])
    [[(6, 20), (23, 29), (30, 35)], [(19, 31)], [(28, 32)], [(5, 40)]]
    """
    # sorts into => [(6, 20), (23, 29), (19, 31), (28, 32), (30, 35), (5, 40)]
    sched = []
    i = 0
    seen = [False] * len(jobs)
    jobs.sort(key = lambda x: x[1])
    for i in range(len(seen)):
        if seen[i] == False:
            sched.append([jobs[i]])
            seen[i] = True
            for j in range(len(jobs)):
                if seen[j] == False and jobs[j][1] > sched[-1][-1][1] and jobs[j][0] > sched[-1][-1][1]:
                    sched[-1].append(jobs[j])
                    seen[j] = True
    return sched

################################################################
# Problem 2
# 
# Given a list of string (strings)
# Find s short string (bigstring) that 
# for every s in string, s is a substring of bigstring.
#
# Use the approximation algorithm we gave in class.
#
# Running Time: 
#
################################################################

def superstring(strings):
    """
    >>> superstring(["CADBC", "CDAABD", "BCDA", "DDCA", "ADBCADC"])
    'BCDAABDDCADBCADC'
    """
    supa = ''
    
    
    return supa

################################################################
# Problem 3
# 
# Find the shortest path from a to b
# in a weighted graph g that is represented by an adjacency matrix.
# You can assume all edge weights are positive.
#
# Running time:
################################################################


# def dijkstra(g, a, b):
#     """
#     >>> g = [ [(1,3), (2,6)], \
#               [(0,3), (4,4)], \
#               [(0,6), (3,2), (5,7)], \
#               [(2,2), (4,4), (8,1)], \
#               [(1,4), (3,4), (6,9)], \
#               [(2,7), (6,2), (7,8)], \
#               [(4,9), (5,2), (9,4)], \
#               [(5,8), (8,3)], \
#               [(3,1), (7,3), (9,2)], \
#               [(6,4), (8,2)] ]
#     >>> dijkstra(g,0,9)
#     [0, 2, 3, 8, 9]
#     """
#     pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
