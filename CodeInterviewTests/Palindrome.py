input = ["eaabaaefedf", "accbcca", "db"]


palinSet = {(x, (i, i + 1)) for i, x in enumerate(inp)} | {(x + inp[i + 1], (i, i + 2)) for i, x in enumerate(inp) if
                                                           i < len(inp) - 2 and inp[i] == inp[i + 1]}
print palinSet

palinBag = set()

for inp in input:
    for palin in palinSet:
        char, (start, end) = palin  # how to claim type in python ?
        # print "check:", char, start, end

        while True:
            if start - 1 > 0:
                start -= 1
            else:
                break
            if end + 1 < len(inp):
                end += 1
            else:
                break

            mid = (end - start) // 2 + start
            if (start - end) % 2 == 0:
                leftMid, rightMid = mid, mid
            else:
                leftMid, rightMid = mid, mid + 1

            # print start, leftMid, rightMid, end
            if inp[start:leftMid] == inp[rightMid:end]:
                palinBag.add((inp[start:end], (start, end)))
            else:
                break

        palinSet = palinSet | palinBag
        palinDict = dict(palinSet)
    palindromes = palinDict.keys()
    print len(palindromes), palindromes

# inp = input[0]
#
# t = 2, 3
# print range(*t), t
#
# a, b = t
# print a, b, "abcdefg"[1:2]





# palin = dict({( (i, i+1),x) for i, x in enumerate(inp) })
# for key, val in dict.iteritems():
# print palin, len(palin)

# palin = dict()
#
# for index, char in enumerate(inp):
#     # palin[char] = (index, index+1)
#     palin[(index, index+1)] = char
#     growPalindrome(inp, palin, index)





#
# def growPalindrome(word, tupleRange, palin=dict()): # palin will be shared across function calls
#     start, end = tupleRange
#     if start - 1 > 0:
#         newStart -= 1
#     else:
#         return
#     if end + 1 < len(word):
#         newEnd += 1
#     else:
#         return
#
# newPalin = word[start, end]
