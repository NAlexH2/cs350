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
# Running Time: O(n^2)
#
################################################################


# def schedule(jobs):
#     """
#     >>> schedule([(5,40), (30,35), (6,20), (19, 31), (23, 29), (28, 32)])
#     [[(6, 20), (23, 29), (30, 35)], [(19, 31)], [(28, 32)], [(5, 40)]]
#     """
#     # sorts into => [(6, 20), (23, 29), (19, 31), (28, 32), (30, 35), (5, 40)]
#     sched = []
#     i = 0
#     seen = [False] * len(jobs)
#     jobs.sort(key = lambda x: x[1])
#     for i in range(len(seen)):
#         if seen[i] == False:
#             sched.append([jobs[i]])
#             seen[i] = True
#             for j in range(len(jobs)):
#                 if seen[j] == False and jobs[j][1] > sched[-1][-1][1] and jobs[j][0] > sched[-1][-1][1]:
#                     sched[-1].append(jobs[j])
#                     seen[j] = True
#     return sched

################################################################
# Problem 2
# 
# Given a list of string (strings)
# Find s short string (bigstring) that 
# for every s in string, s is a substring of bigstring.
#
# Use the approximation algorithm we gave in class.
#
# Running Time: O(n^4)
#
################################################################

# def superstring(strings):
#     """
#     >>> superstring(["CADBC", "CDAABD", "BCDA", "DDCA", "ADBCADC"])
#     'BCDAABDDCADBCADC'
#     >>> superstring(["catg", "ctaagt", "gcta", "ttca", "atgcatc"])
#     'gctaagttcatgcatc'
#     >>> superstring(["Tough", "questions", "asked"])
#     'Toughquestionsasked'
#     """
#     sts = strings


#     used = [False] * len(sts)
#     sizematch = 0
    
#     # It works, but doesn't produce the exact string from the test.
#     # In some cases finds an even shorter super string that's still valid.
#     for i in range(len(sts)):
#         if sts[i] != None:
#             for j in range(len(sts[i])):
#                 for k in range(len(sts)):
#                     if k != i and sts[k] != None:
#                         for l in range(len(sts[k])):
#                             if sts[i][j] == sts[k][l]:
#                                 sizematch += 1
#                             if j == len(sts[i])-1 or l == len(sts[k])-1:
#                                 if sizematch > 0:
#                                     sts[i] = sts[i] + sts[k][sizematch:]
#                                     sts[k] = None
#                                     sizematch = 0
#                                 else:
#                                     sts[i] = sts[i] + sts[k]
#                                     sts[k] = None
#                                     sizematch = 0              
#     return sts[0]

################################################################
# Problem 3
# 
# Find the shortest path from a to b
# in a weighted graph g that is represented by an adjacency matrix.
# You can assume all edge weights are positive.
#
# Running time: O((V+E) * p(v))
################################################################
def dijkstra(g, a, b):
    """
    >>> g = [ [(1,3), (2,6)], \
              [(0,3), (4,4)], \
              [(0,6), (3,2), (5,7)], \
              [(2,2), (4,4), (8,1)], \
              [(1,4), (3,4), (6,9)], \
              [(2,7), (6,2), (7,8)], \
              [(4,9), (5,2), (9,4)], \
              [(5,8), (8,3)], \
              [(3,1), (7,3), (9,2)], \
              [(6,4), (8,2)] ]
    >>> dijkstra(g,0,9)
    [0, 2, 3, 8, 9]
    """
    
    path = []
    path.append(a)
    # for i in range(len(g)):
        
    
    
    return path


if __name__ == "__main__":
    import doctest
    doctest.testmod()
