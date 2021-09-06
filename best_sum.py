def best_sum(target_sum, arr,memo = dict()):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    shortest_combination = None
    for num in arr:
        remainder = target_sum - num
        remainder_combination = best_sum(remainder,arr,memo)
        if remainder_combination is not None:
            combination = [*remainder_combination, num]
            if shortest_combination == None or len(combination) < len(shortest_combination):
                shortest_combination = combination
    memo[target_sum] = shortest_combination
    return shortest_combination  

print(best_sum(7,[5,3,4,7]))
print(best_sum(100,[1,2,5,25]))