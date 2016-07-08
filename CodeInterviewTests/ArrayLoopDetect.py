# directional graph presented in array format, find loop if present

from random import shuffle

# shuffled range array, must have loop
a = range(21)
shuffle(a)
print a
print range(20)

# a = [10, 15, 11, 6, 19, 12, 4, 2, 18, 5, 7, 8, 16, 17, 13, 9, 14, 3, 0, 1]

# DFS?  -> extra memory version
def loop_detect_w_extra_memory(a):
    visited = [False] * len(a)

    i = 0
    el = a[0]
    while True:
        if visited[i] == True:
            print "Have visited ", i, ". There is a loop"
            break
        else:
            visited[el] = True
            i = el
            el = a[el]


loop_detect_w_extra_memory(a)


# 2 chasing pointers
def move_p(a, p):
    if p < 0 or p >= len(a):
        raise ValueError("invalid input array")
    return a[p]

# for a chasing pointer problem, every time those 2 pt will meet at the index 0
def chasing_pointer(a):
    p1 = p2 = 0
    while True:
        p1 = move_p(a, p1)
        p2 = move_p(a, move_p(a, p2))
        print p1, p2
        if p1 == p2:
            print "Loop detected at ", p1
            break

chasing_pointer(a)