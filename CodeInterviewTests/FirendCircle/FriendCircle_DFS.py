# There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature, i.e., if A is friend of B and B is friend of C, then A is also friend of C. A friend circle is a group of students who are directly or indirectly friends. You are given a N×N−matrix M which consists of characters Y or N. If M[i][j]=Y, then ith and jth students are friends with each other, otherwise not. You have to print the total number of friend circles in the class.


dim = 5
print xrange(dim), range(dim)

# todo, check how to create a real package.
# check find and filter for python collections.
#

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
def DFS_visit( i, visited, circleNodes):
    visited[i] = True
    circleNodes.append(i)
    nonVisitedFriend = [j for j in xrange(len(visited)) if not visited[j] and getValue_symetric_matrix(i, j) == "Y" and i != j]
    for f in nonVisitedFriend:
        visited[f] = True
    for f in nonVisitedFriend:
        visited = DFS_visit(f, visited, circleNodes)
    return visited

def DFS(i, visited, parentNode):
    neighbors = [j for j in xrange(len(visited)) if getValue_symetric_matrix(i, j) == "Y" and i != j]
    for nei in neighbors:
        if visited[nei] != "notVisited":
            visited[nei] = "touched"
            parentNode[nei] = i
            DFS(nei, visited, parentNode)
    visited[i] = "finished"


circles = 0
circleList = set()
visited = [False] * dim
unvisited = range(dim)
while len(unvisited):
    circleNodes = list()
    visited = DFS_visit(unvisited[0], visited, circleNodes)
    unvisited = [k for k, val in enumerate(visited) if not val]
    circles += 1
    circleList.add(tuple(circleNodes))

print circles, circleList

# when the model is loaded as main
if __name__ == "__main__":
    print "this is a main"





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