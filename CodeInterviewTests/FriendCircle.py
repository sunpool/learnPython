dim = 5
print xrange(dim), range(dim)

# non directional graph connection is symmetric
non_directional = ["YYYXX", "YXXY", "XYY", "XY", "X"]
dim = len(non_directional)


def getValue_symetric_matrix(i, j, matrix=non_directional):
    # print "input", i, j
    if i <= j:
        row = i
        col = j - i
    else:
        row = j
        col = i - j
    # print "getVa", row, col
    # print
    return matrix[row][col]


# print out all circles in graph,
# visited = [[False]*dim]*dim
# visited = [[False for i in xrange(dim)] for j in xrange(dim)]

# python 3+ xrange is off, and range become xrange that without instantiate a list. can be forced to list as list(range(10))
visited = [False] * dim
# visited = [False for i in xrange(dim)]

# loop DFS
# stack = [0]
from collections import deque
queue = deque([0])
circle = []
circles = set()
# visited[0] = True
# for i in xrange(dim):˚
while len(queue):
    # i = stack.pop()
    i = queue.popleft()
    circle.append(i)
    if not visited[i]:
        print i
        connected = [j for j in xrange(dim) if i != j and getValue_symetric_matrix(i, j) == "Y"]
        print connected
        queue.extend(connected)
        # print queue
        visited[i] = True
    else:
        circles.add(tuple(circle))
        circle = list()


print circles



