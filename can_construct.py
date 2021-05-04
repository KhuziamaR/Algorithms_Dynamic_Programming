def can_construct(target,word_bank,memo = dict()):
    if target in memo:
        return memo[target]
    if target == '':
        return True
    for string in word_bank:
        if target.startswith(string):
            remainder = target[len(string)::]
            if can_construct(remainder,word_bank,memo) == True:
                memo[target] = True
                return True
    memo[target] = False
    return False

print(can_construct("abcdef",["ab","abc","cd","def","abcd"]))
print(can_construct("skateboard",["bo","rd","ate","t","ska","sk","boar"]))
