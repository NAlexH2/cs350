# Today was all about dynamic programming which involved a lot of coding smaller
# programs more than actual notes.

def test(g):
    """
    >>> test(1)
    1
    """
    return g
#THIS CODE MAY NOT FUNCTION RIGHT. BE WARNED.

#example of slide 18 done in class
def choose(n,k):
    """
    >>> choose(10,3)
    120
    """
    memo = [[None] * (k+1) for i in range(n+1)]
    return choose_rec(n, k, memo)

def choose_rec(n,k,memo):
    if memo[n][k] is not None:
        return memo[n][k]
    
    if k == 0 or k == n:
        memo[n][k] = 1
        return 1
    
    else:
        val = choose_rec(n-1,k,memo) + choose_rec(n-1,k-1,memo)
        memo[n][k] = val
        return val
########END EXAMPLE

#knapsack problem (slide 22)
#it = items, c = capacity
# memo = best set of values that can fit into c
# memo doesn't have to be a matrix for this case
# running time = O(nW) n = items, W = capacity
def knapsack(it, c):
    """
    >>> knapsack([[1000,7],[1000,7],[500,4]], 20)
    ???
    """
    memo = [[None] * c for i in it] #n = item number of rows, capacity number of columns
    return knapsack_rec(it, 0, c, memo)

def knapsack_rec(it, i, c, memo):
    if memo[i][c] is not None:
        return memo[i][c]
    if i == len(it):
        memo[c] = 0
        return 0
    
    else:
        if it[i][1] <= c:
            val = max(knapsack(it, i+1, c-it[i][1], memo) + it[i][0], knapsack(it, i+1, c, memo))
            memo[i][c] = val
            return val
        
        else:
            val = knapsack(it, i+1, c)
            memo[i][c] = val
            
########END EXAMPLE

#Making change problem (slide 26)
#given target amount of t, give fewest coins possible
#cs = coin denmoinations, t = target value
# running time = O()
def makeChange(cs,t):
    pass

def mC(cs, t):
    if t == 0:
        return 0
    fewCoins = t
    for c in cs:
        coins = mC(cs,t-c)+1
        fewCoins = min(fewCoins, coins)
    
    return fewCoins
        


########END EXAMPLE
if __name__ == "__main__":        
    import doctest
    doctest.testmod()