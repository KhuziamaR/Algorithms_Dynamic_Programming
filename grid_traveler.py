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

# print(grid_traveler(18,18))

def grid_traveler_tab(m,n):
    table = [(m+1)*[0] for i in range(n+1)]
    table[1][1] = 1
    for i in range(m+1):
        for j in range(n+1):
            current = table[i][j]
            if ( j+1 <= n):
                table[i][j+1] += current
            if (i+1 <= m):
                table[i+1][j] += current
    return table[m,n]


print(grid_traveler(18,18))

    
# print([4*[0] for i in range(4)])