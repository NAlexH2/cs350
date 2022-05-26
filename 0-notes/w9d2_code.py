# running time for backtracking soln is O(n!) (worst case)
# python3 -i w9d2_code.py

###Example one
# Possible way to place queens on the board
# in a way they cannot take eachother based on an nxn grid decided
# exclusively by the columns

def queens(n):
    return queens_rec([], n)
     

def queens_rec(qs, n):
    if len(qs) == n:
        print(qs)
        return qs
    
    for i in range(n): # represents the rows
        if i not in qs and safe(qs, i): # represents the columns
            qs.append(i)
            candidate = queens_rec(qs, n)
            if candidate is not None:
                return candidate
            qs.pop()

    return None  
    
def safe(qs, c):
    # c = column attempting to add to, qc = current queen column
    # r = row attempting to add to, qr = current queen column
    r = len(qs) # row position adding to
    for qr in range(len(qs)):
        # |r-c| = |qr-qc|
        qc = qs[qr]
        if abs(r-qr) == abs(c-qc):
            return False

    return True

# Example two
# Traveling salesman modified from n queens

g = [ [  0, 8, 15,  3,  8], \
      [  8, 0,  3, 12,  9], \
      [ 15, 3,  0,  7,  6], \
      [ 14,12,  7,  0, 16], \
      [  8, 9,  6, 16,  0]]

def TSP(g):
    minPathWeight = g[-1][0]
    for i in range(len(g) - 1):
        minPathWeight += g[i][i+1]
    return TSP_rec(g, [0], 0, minPathWeight, list(range(len(g))))

# backtracking - make a change, if the change turns out to be bad, undo the
# change and try something else

# this method is branch and bound or something
def TSP_rec(g, vs, w, feasibleWeight, feasiblePath):
    if w > feasibleWeight:
        return (feasibleWeight, feasiblePath)
    if len(vs) == len(g):
        return (w+g[vs[-1]][vs[0]], vs)

    for i in range(len(g)):
        if i not in vs:
            (pathWeight, path) = TSP_rec(g, vs + [i], w + g[vs[-1]][i], feasibleWeight, feasiblePath)
            if pathWeight < feasibleWeight:
                feasibleWeight = pathWeight
                feasiblePath = path
            # run the for loop to check another vertex in the neighborhood
    return (feasibleWeight, feasiblePath)
