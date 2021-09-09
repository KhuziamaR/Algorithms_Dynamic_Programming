def can_sum(target_sum,arr,memo = dict()):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    for num in arr:
        if can_sum(target_sum-num,arr,memo) == True:
            memo[target_sum] = True
            return True
    memo[target_sum] = False
    return False
        
print(can_sum(0,[1,1]))
