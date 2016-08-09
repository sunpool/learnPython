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
            del_key = min(self.sore, key=self.store.get)  # nlogn, not optimal
            del self.store[del_key]

        self.store[key] = val
        self.LRU_count.setdefault(key,0)
        self.LRU_count[key] += 1
        return self.store[key]

LRU = LRU_cache()

print LRU.get("hey ")

print LRU.set("ha", 20)

print  LRU.get("ha"), LRU,