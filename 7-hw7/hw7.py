# CS 350: Homework 7
# Due: Week of 5/23
# Name: Alex Harris

import heapq as hq

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
# Running Time: O(n^(2*words))
#
################################################################
def overlap(str1, str2, cstr):
    # cstr is common string - str1 + str2 or str2 + str1 depedning on the result
    # of the loops
    overlap = 0 # count the overlaps that occur based on i loops
    len1 = len(str1) # shrink down typing
    len2 = len(str2) # same
    
    # if the last part of str1 lines up with the first part of str2
    for i in range(min(len1, len2)):
        if str1[len1-i:] == str2[:i]:
            if overlap < i:
                overlap = i
                cstr = [str1 + str2[overlap:]]
    
    # if the first part of str1 linues up with the last part of str2
    for i in range(min(len1, len2)):
        if str1[:i] == str2[len2-i:]:
            if overlap < i:
                overlap = i
                cstr = [str2 + str1[overlap:]]

    #it turns out I didn't need to append, but if I change this it will 
    # change the rest of the codes logic and break the program. In a
    # production based environment I'd fix this, but it's for school
    cstr.append(overlap)
    return cstr

def superstring(strings):
    """
    >>> superstring(["CADBC", "CDAABD", "BCDA", "DDCA", "ADBCADC"])
    'BCDAABDDCADBCADC'
    >>> superstring(["catg", "ctaagt", "gcta", "ttca", "atgcatc"])
    'gctaagttcatgcatc'
    >>> superstring(["Tough", "questions", "asked"])
    'Toughquestionsasked'
    """
    sts = strings # shorthand strings
    ovl = [] # track the overlapped word
    sss = set() # use a set to see if we've made words before
    
    # track the word and its largest overlap size that occured. 
    # -999 used as a nuclear option
    largestyet = ['', 999*-1] 
    sSize = len(strings) # used to ensure we've done the loops enough times
    # to check every possibility
    
    first = last = 0 # used if largestyet[1] never got a value bigger than 0


    # While we haven't visited every single spot
    while sSize > 1:
        sSize -= 1 # We've started being at a spot, so one less to go.
        
        # loop through the list
        for i in range(len(sts)):
                # loop through the list starting at i + 1
                for j in range(i+1, len(sts)):
                    
                        # Deduce our overlaps if any
                        ovl = overlap(sts[i], sts[j], [])
                        # if ovl got more than it bargained for...
                        if len(ovl) > 1 and ovl[1] > largestyet[1] and ovl[0] not in sss:
                            # Hold on to that thing for dear life
                            largestyet[0] = ovl[0]
                            largestyet[1] = ovl[1]
                            
                        # Otherwise, just like track the two things we're
                        # at in the loop in the event we leave early and gotta
                        # make stuff work
                        if len(ovl) == 1:
                            first = i
                            last = j

        # The magic! Largestyet does have a value larger than 0 in it's 1st ind
        # so we want to set strings 0th index to it and re-traverse all over
        # again when we're done here. We also want to add largestyet to our
        # superstringset set just to ensure any future largestyets are not
        # evaluated.
        if largestyet[1] > 0:
            sts[0] = largestyet[0]
            sss |= {largestyet[0]}
            largestyet = ['', 999*-1] # reset, might have more loops to do
            
        # Otherwise, it turns out we never got a largest yet so there wasn't a
        # single overlap for our strings 0th index at all
        else:
            if sts[first] not in sts[0]:
                sts[0] += sts[first]
            if sts[last] not in sts[0]:
                sts[0] += sts[last]
            sss |= {sts[0]}
            
    # Send it home
    return sts[0]

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
    dist = [float('inf')] * (b+1) # dist = weight
    dist[a] = 0 # set the initial starting position to 0 dist from itself
    seen = [False] * (b+1) # Track our visits in the list
    visitedQ = [(a,0)] # the heap to be used to traverse the graph
    
    # dictates the parent node of the node we are currently at
    pnode = [float('inf')] * (b+1)
    
    # While we have and are able to push items onto our visitedQ
    while visitedQ:
        
        # Focus efforts one node at a time, take the one with the smallest
        u = hq.heappop(visitedQ)
        if seen[u[0]] != True: #[0] since I know that's my node
            # mark it seen asap, we do not want to risk retraversal
            seen[u[0]] = True
            
            # This is a bit interesting - for ever vertex in my graph at node
            # u[0] (need to spec. index since it's a toupe at visitedQ)... 
            for v in g[u[0]]:
                
            # make sure that we... 
            # 1: haven't been here before
            # 2: that the weight (dist) + weight of its neighbor 
            # (the node we are currently evaluating against the parent) 
            # is less than the parrent + current nodes value
                if seen[v[0]] == False and dist[u[0]] + v[1] < dist[v[0]]:
                    
                    # store the dist on path u~v in a seperate location
                    # at the current nodes index in dist
                    dist[v[0]] = dist[u[0]] + v[1]
                    # save the parent node of current node
                    pnode[v[0]] = u[0] 
                    
                    # Push onto visitedQ the current node, and it's weight 
                    # so that when we come back to the if, we have something
                    # to evaluate.
                    hq.heappush(visitedQ, (v[0], dist[v[0]]))

                    # start the for loop over if there's more items at the
                    # current node
                    
    # This makepath will take any "b" and find the path to it via pnode. 
    return makepath(pnode, b, [])

def makepath(pn, pf, pnp):
    # pn = parent node/pnode, f = parent finder, pnp = pnode path
    if pf == float('inf'):
        return
    makepath(pn, pn[pf], pnp)
    pnp.append(pf)
    return pnp
        


if __name__ == "__main__":
    import doctest
    doctest.testmod()
