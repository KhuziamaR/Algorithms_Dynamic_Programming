for i in range(len(target)+1):
        if len(table[i]) > 0:
            for word in wordBank:
                if target[i:i+len(word)] == word:
                    if i + len(word) <= len(target):
                        table[i + len(word)].append([*table[i],word])
    return table[len(targ