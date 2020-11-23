from collections import OrderedDict
import sys

class Caching_least(object):

    def __init__(self, capacity):
        if not capacity:
            sys.exit('Capacity below the limit')
        
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            #Move item to the end because it is recently used.
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def set(self, key, value):
        #Pop LRU item from cache if it exceeds capacity
        self.cache.popitem(last=False) if len(self.cache) == self.capacity else None

        # Add item to cache and move it to the end because it is recently used.
        self.cache[key] = value
        self.cache.move_to_end(key)
        

our_cache = Caching_least(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Edge Test
our_cache1 = Caching_least(0) #Returns Capacity less than zero and exits.