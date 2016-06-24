
from __future__ import print_function

a = ["aaabbbkkh", "cceedfg"]

# print a;

for word in a:
    tmp = ""
    num = 0
    for char in word:
        if tmp == char:
            num += 1
        else:
            if num > 1:
                print ( num, end="" )
                num = 0
            tmp = char
            print char, end = ""

