from collections import deque

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "hox", "lot", "log"]
wordSet = set(wordList)

childDict = dict()


# def BFS_build( beginWord, endWord, wordSet = wordSet, childDict ):
def searchNextLevel(children, endWord, wordSet, childDict):
    stop = False
    gChildren = set()
    hitword = set()

    # print "wordset", wordSet

    for word in children:
        for i, char in enumerate(word):
            for j in xrange(26):
                nWord = word[0:i] + chr(ord("a") + j) + word[i + 1:]
                if nWord == endWord:
                    stop = True
                    if word not in childDict:
                        childDict[word] = []
                    childDict[word].append(nWord)
                    hitword.add(word)
                    # print "hit word", word, nWord, endWord

                # if len(wordSet) == 0:
                #     return set()

                if nWord in wordSet:
                    wordSet.remove(nWord)
                    if word not in childDict:
                        childDict[word] = []
                    childDict[word].append(nWord)
                    gChildren.add(nWord)
    if not stop:
        return searchNextLevel(gChildren, endWord, wordSet, childDict)
    else:
        return hitword


begin_word_tree = dict()
leaveWords = searchNextLevel([beginWord], endWord, set(wordList), begin_word_tree)

end_word_tree = dict()
rootwords = searchNextLevel([endWord], beginWord, set(wordList), end_word_tree)

print childDict, wordSet
print "begin tree", begin_word_tree
print "end tree", end_word_tree
print leaveWords, rootwords


# beginWord scoped
def DFS_travers(leave, acc):  # , beginword):
    if leave == beginWord:
        print [leave] + acc
        return
        # return leave

    # parents = end_word_tree[leave]  # will throw if not exist
    parents = end_word_tree.get(leave, [])
    for par in parents:
        DFS_travers(par, [leave] + acc)
        # print leave


for endDict in leaveWords:
    DFS_travers(endDict, ["cog"])
