dim = 5
print xrange(dim), range(dim)

# non directional graph connection is symmetric
non_directional = ["YYYXX", "YXXY", "XYY", "XY", "X"]
dim = len(non_directional)


def getValue_symetric_matrix(i, j, matrix=non_directional):
    print "input", i, j
    if i <= j:
        row = i
        col = j - i
    else:
        row = j
        col = i - j
    print "getVa", row, col
    print
    return matrix[row][col]


# print out all circles in graph,
# visited = [[False]*dim]*dim
# visited = [[False for i in xrange(dim)] for j in xrange(dim)]

# python 3+ xrange is off, and range become xrange that without instantiate a list. can be forced to list as list(range(10))
visited = [False] * dim
# visited = [False for i in xrange(dim)]

# loop DFS
stack = [0]
visited[0] = True
for i in xrange(dim):
    print i
    connected = [j for j in xrange(dim) if getValue_symetric_matrix(i, j) == "Y"]
    print connected
