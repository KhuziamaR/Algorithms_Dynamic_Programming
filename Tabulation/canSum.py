def canSum(target, numbers):
    cache = [None] * (target + 1)
    cache[0] = []
    for i in range(target + 1):
        if cache[i] is not None:
            for num in numbers:
                combination = [*cache[i],num]
                if i + num <= target:
                    if not cache[i + num] or len(combination) < len(cache[i + num]):
                        cache[i + num] = combination

    return cache[target]

print(canSum(15,[3,3,1,10,5]))