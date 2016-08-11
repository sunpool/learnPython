# plain dict implementation
class LRU_cache():
    def __init__(self, capacity=50):
        self.store = {}
        self.LRU_count = {}
        self.capacity = capacity

    def get(self, key):
        if key in self.store:
            self.LRU_count[key] += 1
            return self.store.get(key)
        else:
            return -1

    def set(self, key, val):
        if len(self.store) == self.capacity:
            del_key = min(self.store, key=self.store.get)  # nlogn, not optimal
            del self.store[del_key]

        self.store[key] = val
        self.LRU_count.setdefault(key, 0)
        self.LRU_count[key] += 1
        return self.store[key]


LRU_cache_heap = LRU_cache(2)


print LRU_cache_heap.set("x", 20), LRU_cache_heap.get('x')
print LRU_cache_heap.set("x", 1),  LRU_cache_heap.set("y", 1)
print LRU_cache_heap.store
print LRU_cache_heap.set("z", 1)
print LRU_cache_heap.store




# use heapq
#   drawback: internal storage can go beyond capacity, as the deleted ones are only marked as dead
#             instead of being really deleted
import heapq


# import itertools

class LRU_heap():
    REMOVED = "<Removed Entry>"

    def __init__(self, capacity):
        self.heap = []
        self.store = {}
        self.capacity = capacity
        # self.counter = itertools.count()

    def set(self, key, val):
        count = 0
        if key in self.store:
            count = self.store[key][0]
            self.__delete_old_keyVal(key)
        elif len(self.store) == self.capacity:
            self.__pop_LR()

        entry = [count + 1, key, val]
        self.store[key] = entry
        heapq.heappush(self.heap, entry)
        return self.store[key][-1]

    def __delete_old_keyVal(self, key):
        entry = self.store[key]
        del self.store[key]
        entry[1] = self.REMOVED

    def __pop_LR(self):
        key = self.REMOVED
        while key == self.REMOVED:
            count, key, val = heapq.heappop(self.heap)
        del self.store[key]

    def get(self, key):
        if key in self.store:
            count, key1, val = self.store[key]
            self.__delete_old_keyVal(key)
            entry = [count + 1, key, val]
            self.store[key] = entry
            heapq.heappush(self.heap, entry)
            return self.store.get(key)

        raise KeyError("no such key")

LRU_cache_heap = LRU_heap(2)

print "Heap implementation: "
try:
    print LRU_cache_heap.get("a")
except KeyError as ke:
    print "no such key warning: ", ke
else:
    raise

print LRU_cache_heap.set("x", 20), LRU_cache_heap.get('x')
print LRU_cache_heap.set("x", 1),  LRU_cache_heap.set("y", 1)
print LRU_cache_heap.store
print LRU_cache_heap.set("z", 1)
print LRU_cache_heap.store


