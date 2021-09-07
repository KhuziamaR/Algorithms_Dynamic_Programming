def countConstruct(target,wordBank):
    table = [0] * (len(target) + 1)
    table[0] = 1
    for i in range(len(target) + 1):
        if table[i] > 0:
            for word in wordBank:
                if target[i:i+len(word)] == word:
                     if (i + len(word)) <= len(target):
                        table[i + len(word)] += table[i]
    print(table)
    return table[len(target)]

# print(countConstruct('purple',['purp','p','ur','le','purpl']))

def allConstruct(target,wordBank):
    table = [[] for i in range(len(target)+1)]
    table[0] = [[]]
    for i in range(len(target)+1):
        for word in wordBank:
            if target[i:i+len(word)] == word:
                if i + len(word) <= len(target):
                    combinations = map(lambda sub: [*sub,word], table[i])
                    table[i + len(word)].extend([*combinations])
    return table[len(target)]

print(allConstruct('purple',['purp','p','ur','le','purpl']))
