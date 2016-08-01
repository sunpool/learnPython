from collections import deque

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "hox", "lot", "log"]
wordSet = set(wordList)

childDict = dict()  # implementation 1
parentDict = dict()  # implementation 2


def component_ensure(mymay, key, default):
    if key not in mymay:
        mymay[key] = default
    return mymay[key]


# def BFS_build( beginWord, endWord, wordSet = wordSet, childDict ):
def searchNextLevel(children, endWord, wordSet, parentDict):
    stop = False
    gChildren = set()
    hitword = set()

    for word in children:
        for i, char in enumerate(word):
            for j in xrange(26):
                nWord = word[0:i] + chr(ord("a") + j) + word[i + 1:]
                if nWord == endWord:
                    stop = True

                    component_ensure(parentDict, nWord, [])
                    parentDict[nWord].append(word)

                    hitword.add(word)

                if nWord in wordSet:
                    # wordSet.remove(nWord)   # wrong! This will remove other equal depth paths, should do after this level is done

                    component_ensure(parentDict, nWord, [])
                    parentDict[nWord].append(word)

                    gChildren.add(nWord)

    for word in gChildren:  # remove redundant after this level is done
        wordSet.remove(word)

    if not stop:
        return searchNextLevel(gChildren, endWord, wordSet, childDict)
    else:
        return hitword


# beginWord scoped
def DFS_travers(leave, acc):  # , beginword):
    if leave == beginWord:
        print [leave] + acc
        return
        # return leave

    # parents = end_word_tree[leave]  # will throw if not exist
    # parents = end_word_tree.get(leave, [])
    parents = parentDict.get(leave, [])

    for par in parents:
        DFS_travers(par, [leave] + acc)
        # print leave



begin_word_tree = dict()
leaveWords = searchNextLevel([beginWord], endWord, set(wordList), begin_word_tree)

for leave in leaveWords:
    DFS_travers(leave, ["cog"])
