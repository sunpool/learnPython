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


# DFS
stack = []
visited = [False] * dim

def DFS_visit( i, visited):
    visited[i] = True
    nonVisitedFriend = [j for j in xrange(len(visited)) if not visited[j] and getValue_symetric_matrix(i, j) == "Y" and i != j]
    for f in nonVisitedFriend:
        visited[f] = True
    for f in nonVisitedFriend:
        visited = DFS_visit(f, visited)
    return visited


unvisited = [k for k, val in enumerate(visited) if not val]
circles = 0
while len(unvisited):
    visited = DFS_visit(unvisited[0], visited)
    unvisited = [k for k, val in enumerate(visited) if not val]
    circles += 1

print circles




# print visited
# stack.append(0)
# visited[0]
# while len(stack):
#     i = stack.pop()
#     # visited[i]= True
#     visited = DFS_visit(i, visited)
    # todo, how-to use filter in python collection
    # nonVisitedFriend = [j for j in xrange(dim) if not visited[i] and getValue_symetric_matrix(i, j) == "Y" and i != j]
    # for f in nonVisitedFriend:
    #     visited[f] = True
    #     visited = DFS_visit(f, visited)
    # stack.extend(nonVisitedFriend)