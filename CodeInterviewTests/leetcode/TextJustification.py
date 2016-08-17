"""
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
"""

words = ["This", "is", "an", "example", "of", "text", "justification."]
L = 16

# reduce(lambda x: len(x), new_line, 0) + len(new_line) - 1

lines = []
num_of_chr = []

length = len(words[0])
new_line = [words[0]]

# for i, word in enumerate(words):  # add 1st word, dont need " "
for i in xrange(1, len(words)):
    word = words[i]
    added_len = len(word) + 1

    if length + added_len <= L:
        new_line.append(word)
        length += added_len
    else:
        lines.append(new_line)
        num_of_chr.append(length)

        new_line = [word]
        length = len(word)

lines.append(new_line)

print lines

strLines = []
for i, line in enumerate(lines[:len(lines) - 1]):
    base_space = (L - num_of_chr[i]) // (len(line) - 1) + 1
    first_space = (L - num_of_chr[i]) % (len(line) - 1) + base_space
    print base_space, first_space

    base_space = " " * base_space
    first_space = " " * first_space
    strLine = line[0] + first_space
    for j, word in enumerate(line[1:]):
        strLine += word
        # new index j is looping through [ line[1], line[2], ... ], last entry index is len(lines[i]) - 2
        if j < len(lines[i]) - 2:
            strLine += base_space
    strLines.append(strLine)

lastLine = lines[len(lines) - 1]
strLastLine = reduce(lambda el, rdc: rdc + " " + el, lastLine[1:], lastLine[0])
strLastLine += " " * (L - len(strLastLine))
strLines.append(strLastLine)

print strLines
