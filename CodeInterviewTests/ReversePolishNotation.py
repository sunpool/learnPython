# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
# Some examples:
# ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

inputs = ["2", "1", "+", "3", "*"]
# inputs = ["4", "13", "5", "/", "+"]

operators = set(["+", "-", "*", "/"])

values = []
for val in inputs:

    if val in operators:
        last = int(values.pop())
        last2 = int(values.pop())
        if val == "*":
            ret = last * last2
        elif val == "+":
            ret = last + last2
        elif val == "-":
            ret = last2 - last
        elif val == "/":
            ret = last2 / last
        values.append(ret)
    else:
        values.append(val)

assert (len(values) == 1)
print values
