#!/usr/bin/python3
"""module"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """class"""
    
    def put(self, key, item):
        """method"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """method"""
        if key not in self.cache_data or key is None:
            return None
        return self.cache_data.get(key)
