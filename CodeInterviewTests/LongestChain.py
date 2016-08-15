
dictWord = ["a", "abcd", "cd", "c", "bcd", "abd"]

dictWord.sort(key=lambda x: len(x), reverse=True)
print dictWord

dictWordSet = set(dictWord)

childDict = {}

queue = []


visited = [False] * len(dictWord)

word = dictWord[0]

# children of next level
def find_child(words, dictWordSet):
    '''
    :param words is nodes of this level
    :param dictWordSet unvisited node till this level
    :return all children of next level
    This is to ensure multi-parent to children info is not lost b/c of the order of visit'''
    nchildren = set()
    child2parent = {}
    for word in words:
        for i, char in enumerate(word):
            nword = word[0:i] + word[i+1:]
            if nword in dictWordSet:
                nchildren.add(nword)
                child2parent.setdefault(nword,set())
                child2parent[nword].add(word)
    # check if it is by reference
    dictWordSet = dictWordSet - nchildren
    return child2parent # (nchildren, dictWordSet)  dictwordset is passed in by reference?


    # if nword in dictWordSet:







for word in dictWord:
    if len(dictWordSet) == 0:
        break

    children = set()
    for i, char in enumerate(word):
        nword = word[0:i] + word[i+1:]
        if nword in dictWordSet:
            # childDict.setdefault(word, set())
            # childDict[word].add(nword)
            children.add(word)
    for ch in children:
        childDict[word] = children

            del dictWordSet[nword]
            pass
