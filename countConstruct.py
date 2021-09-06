def countConstruct(target,wordBank, memo = dict()):
    if target in memo:
        return memo[target]
    if target == "":
        return 1
    count = 0
    for word in wordBank:
        if target.startswith(word):
            numWays = countConstruct(target[len(word)::],wordBank, memo)
            count += numWays
    memo[target] = count
    return count

print(countConstruct('abcdef',['abcdef','a','b','c','d','e','f']))