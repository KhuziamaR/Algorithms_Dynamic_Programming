# MEMOIZATION
def fib(n,memo = dict()):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-2,memo) + fib(n-1,memo)
    return memo[n]
    
print(fib(20))

# Tabulation 
def fib_tab(n):
    arr = [0] * (n + 2)
    i = 0
    arr[1] = 1 
    while i < n:
        arr[i+1] += arr[i]
        arr[i+2] += arr[i]
        i += 1
    return arr[n]
print(fib_tab(50))