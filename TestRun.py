x = dict()
x[1] = 2

# x.update(1, 2)
x.setdefault(12, 20)

y = set([2])
print y.union([3]), {2, 3}, float('infinity'), float('-inf'), float('inf')

print {v: k for k, v in x.iteritems()}

print set(p for p in set([(1, 2), (1, 3)]))

print range(3, 0, -1),

print not not {}.get(20)

import heapq

itm = (2, 3, "hello")

hq = []
heapq.heappush(hq, itm )
hey = dict(x=itm)
print hq, hey

del hey["x"]
print hq, hey

x, y, z = [1,2,4]

inputs = ["2", "1", "+", "3", "*"]
print inputs.pop(), inputs, len("justification")

print [1,2,4][1:]

print 0 or 20, 30 or 40


# print [p for p in [{1, 2}, {2, 3}]]
# map(lambda val: print val, {"hey": {1, 2}, "how":{0}})

# print reduce(lambda acc, el: acc.union(el), [p for p in [{1, 2}, {2, 3}, {2, 3}]], set())
