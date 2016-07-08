
dim = 5

# non directional graph connection is symmetric
non_directional = ["YYYXX", "YXXY", "XYY", "XY", "X"]
dim = len(non_directional)

def getValue_symetric_matrix(i,j, matrix= non_directional):
    if i <= j:
        row = i
        col = j
    else:
        row = j
        col = i
    return matrix[row][col]

# print out all circles in graph,
# visited = [[False]*dim]*dim
# visited = [[False for i in xrange(dim)] for j in xrange(dim)]

# python 3+ xrange is off, and range become xrange that without instantiate a list. can be forced to list as list(range(10))
visited = [False]*dim
# visited = [False for i in xrange(dim)]

# loop DFS
stack = [0]
visited[0] = True
for i in xrange(dim):


