def all_construct(target,word_bank, memo = dict()):
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]
    result = []
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word)::]
            suffix_ways = all_construct(suffix,word_bank)
            target_ways = map(lambda way: [word, *way],suffix_ways)
            result.extend(target_ways)
    memo[target] = result
    return result

print(all_construct('purple',['purp','p','ur','le','purpl']))


