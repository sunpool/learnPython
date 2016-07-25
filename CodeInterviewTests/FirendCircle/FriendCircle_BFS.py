

dim = 5
print xrange(dim), range(dim)

# non directional graph connection is symmetric
non_directional = ["YXYXX", "YXXX", "XYY", "XY", "X"]
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
num_circles = 0
# visited[0] = True
# for i in xrange(dim):
while len(queue):
    # i = stack.pop()
    i = queue.popleft()
    # circle.append(i)
    # if not visited[i]:
    print i
    connected = [j for j in xrange(dim) if i != j and getValue_symetric_matrix(i, j) == "Y"]
    unvisited_friends = [k for k in connected if not visited[k]]
    print connected, unvisited_friends
    queue.extend(unvisited_friends)
    # print queue
    visited[i] = True
    # else:
    #     if len(circle) == 1:
    #         if getValue_symetric_matrix(circle[0], circle[0]) == "Y":
    #             circle = list()
    #     else:
    #         circles.add(tuple(circle))
    #         circle = list()
    if not len(queue):
        num_circles += 1
        unvisited = [i for i, val in enumerate(visited) if not val]
        if len(unvisited):
            queue.append(unvisited[0])


print "num of circles", num_circles
print circles



