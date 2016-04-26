class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.tm = 0
        self.cache = {}
        self.lru = {}

    def get(self, key):
        if key in self.cache:
            self.lru[key] = self.tm
            self.tm += 1
            return self.cache[key]
        return -1

    def set(self, key, value):
        if len(self.cache) >= self.capacity:
            # find the LRU entry
            old_key = min(self.lru.keys(), key=lambda k:self.lru[k])
            self.cache.pop(old_key)
            self.lru.pop(old_key)
        self.cache[key] = value
        self.lru[key] = self.tm
        self.tm += 1


import collections

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value

class LRU_Cache:
    def __init__(self, original_function, maxsize=1024):
        # Link structure: [PREV, NEXT, KEY, VALUE]
        self.root = [None, None, None, None]
        self.root[0] = self.root[1] = self.root
        self.original_function = original_function
        self.maxsize = maxsize
        self.mapping = {}

    def __call__(self, *key):
        mapping = self.mapping
        root = self.root
        link = mapping.get(key)
        if link is not None:
            link_prev, link_next, link_key, value = link
            link_prev[1] = link_next
            link_next[0] = link_prev
            last = root[0]
            last[1] = root[0] = link
            link[0] = last
            link[1] = root
            return value
        value = self.original_function(*key)
        if len(mapping) >= self.maxsize:
            oldest = root[1]
            next_oldest = oldest[1]
            root[1] = next_oldest
            next_oldest[0] = root
            del mapping[oldest[2]]
        last = root[0]
        last[1] = root[0] = mapping[key] = [last, root, key, value]
        return value


if __name__ == '__main__':
    p = LRU_Cache(ord, maxsize=3)
    for c in 'abcdecaeaa':
        print(c, p(c))
