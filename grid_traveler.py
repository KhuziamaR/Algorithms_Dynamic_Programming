def grid_traveler(m,n,memo=dict()):
    key = str(m) + ',' + str(n)
    key_inverse = str(n) + ',' + str(m) # n*m grid has same solution as m*n
    if key in memo or key_inverse in memo:
        return memo[key]
    if m == 1 or n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[key_inverse] = grid_traveler(m-1,n,memo) + grid_traveler(m,n-1,memo)
    memo[key] = grid_traveler(m-1,n,memo) + grid_traveler(m,n-1,memo)
    return memo[key]

print(grid_traveler(18,18))