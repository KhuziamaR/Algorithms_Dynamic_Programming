def count_construct(target,word_bank,memo = dict()):
    if target in memo:
        return memo[target]
    if target == '':
        return 1
    count = 0
    for word in word_bank:
        if target.startswith(word):
            num_ways = count_construct(target[len(word)::],word_bank,memo)
            count += num_ways
    memo[target] = count
    return count

print(count_construct('purple',['purp','p','ur','le','purpl']))
print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','e','ee','eeeee','eeee','eeeee','eeeeee']))