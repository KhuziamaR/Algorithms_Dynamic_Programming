def fib(num):
    cache = [0] * (num + 1)
    cache[1] = 1
    for i in range(2,num + 1):
        cache[i] = cache[i-1] + cache[i-2]
    return cache[num]
print(fib(50))