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

def integerConvert(array):
    numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
    numbersCache = {'zero':0,'one':0,'two':0,'three':0,'four':0,'five':0,'six':0,'seven':0,'eight':0,'nine':0}
    numbersRef = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    i = 0
    while i < len(numbers) and len(array) > 0:
        if canConstruct(numbers[i],array):
            for char in numbers[i]:
                array = array.replace(char,"",1)
            numbersCache[numbers[i]] += 1
        else:
            i += 1
    result = ""
    print(numbersCache)
    for key,value in numbersCache.items():
        result += (str(numbersRef[key]) * value)
    return result
            
print(integerConvert('oneninetwoninenine'))

# print(canConstruct("one","oneninetwoninenine"))

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
