values = ["[](){}", "[(){([])}[()]", "[([)]"]

braceMap = {"[": "]", "(": ")", "{": "}",
            "]": "NoMatch", ")": "NoMatch", "}": "NoMatch"
            }

for val in values:
    stack = []
    for char in val:
        # for i in range(len(val)):
        #     char = val[i]
        if len(stack) != 0 and char == braceMap[stack[len(stack) - 1]]:
            stack.pop()
        else:
            stack.append(char)
    if len(stack) == 0:
        print("Yes", )
    else:
        print("No", )
