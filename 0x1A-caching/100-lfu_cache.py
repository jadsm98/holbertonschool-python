#!/usr/bin/python3
"""
LFU Module
"""


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Class
    """

    def __init__(self):
        """
        Init
        """

        super().__init__()
        self.keys = []
        self.uses = {}

    def put(self, key, item):
        """
        Put Method
        """

        if key is not None and item is not None:
            if len(self.keys) == BaseCaching.MAX_ITEMS and \
                    key not in self.keys:
                rem = self.keys.pop(self.keys.index(self.findLFU()))
                del self.cache_data[rem], self.uses[rem]
                print('DISCARD: {}'.format(rem))
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
                self.uses[key] = 0
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
                self.uses[key] += 1

    def get(self, key):
        """
        Get method
        """
        if key is not None and key in self.cache_data:
            self.keys.append(self.keys.pop(self.keys.index(key)))
            self.uses[key] += 1
            return self.cache_data[key]
        return None

    def findLFU(self):
        """
        Find the LFU key
        """

        items = list(self.uses.items())
        freqs = [item[1] for item in items]
        least = min(freqs)

        lfus = [item[0] for item in items if item[1] == least]
        for key in self.keys:
            if key in lfus:
                return key
