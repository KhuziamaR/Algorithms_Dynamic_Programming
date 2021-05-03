def how_sum(target_sum,arr, memo = dict()):
    if target_sum == 0:
        return []
    if target_sum < 0: 
        return None
    for num in arr:
        result = how_sum(target_sum-num,arr, memo)
        if result != None:
            result.append(num)
            memo[target_sum] = result
            return memo[target_sum]
    memo[target_sum] = None
    return None
print(how_sum(7,[2,3]))
print(how_sum(7,[5,3,4,7]))
print(how_sum(7,[2,4]))
print(how_sum(8,[2,3,5]))
print(how_sum(300,[7,14]))
