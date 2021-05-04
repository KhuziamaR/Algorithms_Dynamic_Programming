def can_construct(target,word_bank):
    if target == '':
        return True
    for string in word_bank:
        if target.startswith(string):
            remainder = target[len(string)::]
            if can_construct(remainder,word_bank) == True:
                return True
    return False

print(can_construct("abcdef",["ab","abc","cd","def","abcd"]))