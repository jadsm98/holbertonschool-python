#!/usr/bin/python3
"""
Module FIFO cache
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Class that inherits from BaseCaching
    """

    def __init__(self):
        """
        Method init
        """
        super().__init__()
        self.data = {}
        self.nextin = 0
        self.nextout = 0

    def append(self, key):
        """
        Append Method
        """
        self.nextin += 1
        self.data[self.nextin] = key

    def pop(self):
        """
        Pop method
        """
        self.nextout += 1
        result = self.data.get(self.nextout)
        del self.cache_data[result]
        del self.data[self.nextout]
        print('DISCARD: {}'.format(result))

    def put(self, key, item):
        """
        Add an item in the cache
        """

        if key is not None or item is not None:
            if key not in self.cache_data:
                self.append(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                self.pop()

    def get(self, key):
        """
        Get an item by key
        """

        if key not in self.cache_data or key is None:
            return None
        return self.cache_data.get(key)
