def gridTraveler(m,n):
    table = [[0]*(n+1)]*(m+1)
    table[1][1] = 1
    for i in range(m+1):
        for j in range(n+1):
            curr = table[i][j]
            if j + 1 <= n:
                table[i][j+1] += curr
            if i + 1 <= m:
                table[i+1][j] += curr
            
    return table[m][n]
    

print(gridTraveler(2,2))