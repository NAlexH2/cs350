from heapq import heappush, heappop


g = [ [(1,3), (2,6)], \
              [(0,3), (4,4)], \
              [(0,6), (3,2), (5,7)], \
              [(2,2), (4,4), (8,1)], \
              [(1,4), (3,4), (6,9)], \
              [(2,7), (6,2), (7,8)], \
              [(4,9), (5,2), (9,4)], \
              [(5,8), (8,3)], \
              [(3,1), (7,3), (9,2)], \
              [(6,4), (8,2)] ]

def prim(g):
    # runtime = Theta((V+E)log(E))
    q = []
    heappush(q, (0,0,0))
    seen = set()
    tree = []
    n = len(g)
    # In dijkstra - need to return the path in order.
    # To add that path, just add another structure of a list of integers
    while len(q) > 0:
        (w, p, u) = heappop(q)
        if u not in seen:
            seen.add(u)
            if p != u:
                tree.append((p,u))
            n -= 1
            if n == 0:
                return tree
            for (v,w) in g[u]:
                if v not in seen:
                    heappush(q, (w,u,v)) #u is the parent, the thing we came from to get to v
    return tree


#Runtime: O(EV) <- VERY BAD! Not much better than floyds algo
def kruskal(g):
    # edges = sorted([(w,u,v) for u in range(len(g)) for (v.w) in g[u]])
    # also a way but not very readable 

    edges = []
    for u in range(len(g)):
        for (v,w) in g[u]:
            edges.append((w,u,v))
    edges.sort() 
    sets = [{u} for u in range(len(g))]
    s = list(range(len(g)))
    # sets[s[v]] == set with v in it

    tree = []
    # n = len(g) - 1
    
    for (w,u,v) in edges:
        if u not in sets[s[v]]:
            print(w,u,v)
            print(sets)
            # sets[s[v]].union(sets[s[u]]) <- not recommended for union
            sets[s[v]] |= (sets[s[u]]) # |= is the UNION and assign operator
            for x in sets[s[u]]:
                s[x] = s[v]
            tree.append((u,v))
            if len(tree) == len(g) -1:
                return tree
    return tree