# CS 350: Homework 7
# Due: Week of 5/23
# Name: Alex Harris

import heapq
from multiprocessing.connection import wait

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
#                if seen[j] == False and jobs[j][1] > sched[-1][-1][1] /
#                   and jobs[j][0] > sched[-1][-1][1]:
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
# Running Time: O(n^3)
#
################################################################
def overlap(str1, str2, cstr):
    # cstr is common string - str1 + str2 or str2 + str1 depedning on the result
    # of the loops
    overlap = 0
    len1 = len(str1)
    len2 = len(str2)
    
    for i in range(min(len1, len2)):
        if str1[len1-i:] == str2[:i]:
            if overlap < i:
                overlap = i
                cstr = [str1 + str2[overlap:]]
    
    for i in range(min(len1, len2)):
        if str1[:i] == str2[len2-i:]:
            if overlap < i:
                overlap = i
                cstr = [str2 + str1[overlap:]]

    cstr.append(overlap)
    return cstr

# def moreoverlaps(sts, ovl):
#     for i in 

def superstring(strings):
    """
    >>> superstring(["catg", "ctaagt", "gcta", "ttca", "atgcatc"])
    'gctaagttcatgcatc'
    """
    sts = strings

    # holding onto two possible overlapping strings to run through
    # every permutation of the list to see the next most common overlap....?
    ovl = []
    scss = ''
    largestyet = ['',0]
    sSize = len(strings)

# write a function to find the overlap between strings
# in both directions (front end and back end)
# send back as a list w/ overlap and thet strings overlap
# store that in a list and search for the max in the list, save that index
# use that index to replace either string in the list and set the other to None
# or remove it/pop
# maybe use a set to keep track of what has already been used.
# or seen/visited true/false array
# 
# then a function iterate over all combos of strings in the loop 
# and print them out
# continue to solve from there (return the strings combined together)
# Do bits an pieces man, that's all.

    while sSize != 0:
        for i in range(len(sts)):
            # Start j at the next string in the list so we aren't double checking
            # i forever possibly
            if sts[i] != None:
                for j in range(i+1, len(sts)):
                    if sts[i] != None and sts[j] != None:
                        ovl = overlap(sts[i], sts[j], [])
                        if len(ovl) > 1 and ovl[1] > largestyet[1]:
                            largestyet[0] = ovl[0]
                            largestyet[1] = ovl[1]
                            print(largestyet, sts[i], sts[j], ovl)
                            over2(sts,largestyet[0])
                        # elif len(ovl) == 1:
                        #     if sts[i] not in scss:
                        #         scss += sts[i]
                        #     if sts[j] not in scss:
                        #         scss += sts[j]
                        #     sts[j] = scss
                        #     print(largestyet, sts[i], sts[j], ovl)
        sSize -= 1:
                
    return largestyet

def over2(sts, ly):
    


# run over and over the list until the smallest common super string 

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
# def dijkstra(g, u, v):
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
    
    # path = []
    # path.append(a)
    # visited = set()
    # visited |= set(path)
    # for u in range(len(g)):
    #         visited = visited | {u}
    # use heap, store the vertex in the heap by the weight as a touple 
    # (node, weight)
    # where the weight is the graph up to that node (v)
    # only looking at the first thing in the heap to get the least possible
    # weight on the path.
    # as added to the heap, add to the path
    # thisheap = heapq()
     

if __name__ == "__main__":
    import doctest
    doctest.testmod()
