from math import isinf

points = [(1, 2), (1, 3), (1, 2),
          (1, 1), (2, 2), (3, 3)]

pointSet = set((v, i) for i, v in enumerate(points))

lines = dict()
avoidDict = dict()

for i, n in enumerate(points):
    # after inner loop, all points on one line should already be collected,
    #  -> 1. avoid calc same line, even if it is a new pair
    #  -> 2. calc of duplicate points in later loop can be avoid
    lineP4i = {}
    dups4i = 0

    toAvoid = avoidDict.get(n, set())
    for j in xrange(i + 1, len(points)):
        m = points[j]
        if m in toAvoid:
            continue
        if m == n:
            dups4i += 1
            continue

        (x0, y0) = n
        (x1, y1) = m
        if x0 == x1:
            lineP4i.setdefault((float("inf"), x0), {n})
            lineP4i[(float("infinity"), x0)] = lineP4i[(float("inf"), x0)].union({m})
            print n, m
        else:
            slope = (y0 - y1) / (x0 - x1)
            intercept = y0 - slope * x0
            lineP4i.setdefault((slope, intercept), {n})
            lineP4i[(slope, intercept)] = lineP4i[(slope, intercept)].union({m})

    for k in xrange(i + 1, len(points)):
        m = points[k]
        paired = reduce(lambda acc, el: acc.union(el), [p for p in lineP4i.itervalues() if m in p], set())
        avoidDict.setdefault(m, set())
        avoidDict[m] = avoidDict[m].union(paired)

    # map(lambda s: len(s) + dups4i, lineP4i)   # todo, find how to use map
    for key, ps in lineP4i.iteritems():
        lines.setdefault(key,0)
        lines[key] += len(ps) + dups4i

print lines

# lineCount = {}
#
# for key, val in lines.iteritems():
#     lineCount[key] = len(val)
#
# print lines
# print lineCount
# map((lambda x, y: print x, y), lines)   # how-to ?
