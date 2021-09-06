def bestSum(targetSum, numbers, memo = dict()):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    shortest = None
    for num in numbers:
        remainder = targetSum - num
        remainder_sum = bestSum(remainder,numbers)
        if remainder_sum is not None:
            combination = [*remainder_sum,num]
            if shortest == None or len(combination) < len(shortest):
                shortest = combination
            memo[targetSum] = shortest
    return shortest
print(bestSum(100,[50,75]))