def canConstruct(string, array, memo = dict()):
    if string in memo:
        return memo[string]
    if string == "":
        return 1
    count = None
    for st in array:
        if string.startswith(st):
            size = len(st)
            if canConstruct(string[size::],array) == 1:
                if count == None:
                    count = 1
                else:
                    count += 1
                memo[string] = True
                return memo[string]
    memo[string] = False
    return False

print(canConstruct("a",['aa']))