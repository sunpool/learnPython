from math import isinf

points = [(1, 2), (1, 3), (1, 2),
          (1, 1), (2, 2), (3, 3)]

lines = dict()

for i, n in enumerate(points):
    for j in xrange(i + 1, len(points)):
        overlap = 0
        m = points[j]

        (x0, y0) = n
        (x1, y1) = m
        if x0 == x1:
            lines.setdefault((float("inf"), x0), {(n, i)})
            lines[(float("infinity"), x0)] = lines[(float("inf"), x0)].union({(m, j)})
            print n, m
        else:
            slope = (y0 - y1) / (x0 - x1)
            intercept = y0 - slope * x0
            lines.setdefault((slope, intercept), {(n, i)})
            lines[(slope, intercept)] = lines[(slope, intercept)].union({(m, j)})

lineCount = {}

for key, val in lines.iteritems():
    lineCount[key] = len(val)

print lines
print lineCount
# map((lambda x, y: print x, y), lines)   # how-to ?
