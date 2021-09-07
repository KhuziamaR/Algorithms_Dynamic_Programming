def allContruct(target,wordBank, memo = dict()):
    if target in memo:
        return memo[target]
    if target == "":
        return [[]]
    result = []
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word)::]
            suffix_ways = allContruct(suffix,wordBank, memo)
            target_ways = map(lambda way: [word,*way],suffix_ways)
            result.extend(target_ways)
    memo[target] = result
    return result
print(allContruct('purple', ['purp','p','ur','le','purpl']))
