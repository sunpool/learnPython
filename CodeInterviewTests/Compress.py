
# from __future__ import print_function

a = ["aaabbbbbkkh", "cceedfg"]

# print a;
#
# for word in a:
#     tmp = ""
#     num = 1
#     for char in word:
#         if tmp == char:
#             num += 1
#         else:
#             if num > 1:
#                 print ( num, end="" )
#                 num = 1
#             tmp = char
#             print( char, end = "" )
#     print( "" )

string = ""

for word in a:
    tmp = ""
    num = 1
    for char in word:
        if tmp == char:
            num += 1
        else:
            if num > 1:
                string += str(num)
                num = 1
            tmp = char
            string += char

print string
