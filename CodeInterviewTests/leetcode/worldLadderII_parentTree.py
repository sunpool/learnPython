# https://leetcode.com/problems/word-ladder-ii/

# Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:
#
# Only one letter can be changed at a time
# Each intermediate word must exist in the word list
# For example,
#
# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# Return
#   [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
#   ]
# Note:
# All words have the same length.
# All words contain only lowercase alphabetic characters.



# SOLUTION

from collections import deque

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "hox", "lot", "log"]

# beginWord = "hot"
# endWord = "dog"
# wordList = ["hot", "dog"]

# beginWord = "a"
# endWord = "c"
# wordList = ["b", "c"]

wordSet = set(wordList)

def searchNextLevel(children, endWord, wordSet, parentDict):
    stop = False
    gChildren = set()
    # hitword = set()   // remove leave node record, as improved DFS tree travers

    # don't load identical word on path
    wordSet -= set(children)

    for word in children:
        for i, char in enumerate(word):
            for j in xrange(26):
                nWord = word[0:i] + chr(ord("a") + j) + word[i + 1:]
                if nWord == endWord:
                    stop = True
                    parentDict.setdefault(nWord, [])
                    parentDict[nWord].append(word)
                    # hitword.add(word)
                elif nWord in wordSet:
                    # wordSet.remove(nWord)   # wrong! This will remove other equal depth paths, should do after this level is done
                    parentDict.setdefault(nWord, [])
                    parentDict[nWord].append(word)
                    gChildren.add(nWord)

    # return if no path. otherwise infinite loop
    if len(gChildren) == 0 and not stop:
        return set()

    # flag the word in wordSet as being loaded in tree.
    wordSet = wordSet - gChildren

    if not stop:
        return searchNextLevel(gChildren, endWord, wordSet, parentDict)


# beginWord scoped
def DFS_travers(leave, acc, parentDict):
    new_acc = []
    for a in acc:
        new_acc.append([leave] + a)

    if leave == beginWord:
        return new_acc

    parents = parentDict.get(leave, [])

    paths = []
    for par in parents:
        paths = paths + DFS_travers(par, new_acc, parentDict)
    return paths

# Method Call
begin_word_tree = dict()
leaveWords = searchNextLevel([beginWord], endWord, set(wordList), begin_word_tree)

print begin_word_tree
ret = DFS_travers(endWord, [[]], begin_word_tree)
print ret
