from collections import deque

def dfs(g, u, v):
    """
    >>> g = [[1,2],[0,4],[0,3,5],[2,4,8],[1,3,6],[2,6,7],[4,5,9],[5,8],[3,7,9],[6,8]]
    >>> dfs(g, 0, 9)
    """
    p = dfs_rec(g, u, v, {u}) #pass in u as type = set
    print(p)
    return
        
def dfs_rec(g, u, v, seen):
    if u == v:
        return [v]
    
    for w in g[u]:
        if w not in seen:
            p = dfs_rec(g, w, v, seen | {w}) #union w with set seen
            if p is not None: #if P != none
                return [u]+p
             
    return None

def bfs(g, u, v):
    parent = {u : u}
    queue = deque()
    queue.append(u)
    while not queue:
        w = queue.popleft()
        for x in g[w]:
            if x not in parent:
                parent[x] = w
                queue.append(x)
                if x == v:
                    return makepath(parent)
                
def makepath(p, s, e):
    path = [e]
    while e != s:
        e = p[e]
        path.append(e)
    return path.reverse()

if __name__ == "__main__":        
    import doctest
    doctest.testmod()