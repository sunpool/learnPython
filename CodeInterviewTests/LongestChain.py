dictWord = ["a", "abcd", "cd", "c", "bcd", "abd"]

word_set = set(dictWord)
# word_dict = dict(zip(dictWord, [0] * len(dictWord)))
word_dict = {}

def walk_down_tree(word, word_set, word_dict):

    print "walk down tree ", word
    max_height = 0
    for i, char in enumerate(word):
        nword = word[0:i] + word[i + 1:]
        if nword in word_set:
            if nword in word_dict:
                max_height = max(word_dict[nword], max_height)
            else:
                max_height = max(max_height, walk_down_tree(nword, word_set, word_dict))
    word_dict[word] = max_height + 1
    return max_height + 1

max_height = 0
for word in word_set:
    if len(word) >= max_height:
        print "search longest ", word
        height = walk_down_tree(word, word_set, word_dict)
        max_height = max(height, max_height)
        print ""

print word_dict
print max_height

# dictWord.sort(key=lambda x: len(x), reverse=True)
# print dictWord

# method of growing a tree -> stupid and not efficient
# word = dictWord[0]
#
# # children of next level
# def find_child(words, dictWordSet, child2parent): #, visited):
#     """
#     This is to ensure multi-parent to children info is not lost b/c of the order of visit
#     :param words:nodes of this level
#     :param dictWordSet:dictWordSet unvisited node till this level
#     :param visited:
#     :return: all children of next level
#     """
#     nchildren = set()
#     # child2parent = {}
#     for word in words:
#         for i, char in enumerate(word):
#             nword = word[0:i] + word[i + 1:]
#             if nword in dictWordSet:
#                 # visited[nword] = 1
#                 nchildren.add(nword)
#                 child2parent.setdefault(nword, set())
#                 child2parent[nword].add(word)
#     # check if it is by reference
#     dictWordSet = dictWordSet - nchildren
#     return nchildren
#     # return child2parent  # (nchildren, dictWordSet)  dictwordset is passed in by reference?
#
#
# nchild = [word]
# while len(nchild):
#     nchild = find_child(nchild, dictWordSet, child2parent)
# if len(dictWordSet):


