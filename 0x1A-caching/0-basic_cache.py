#!/usr/bin/python3
"""
Basic_caching module
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic class
    """

    def put(self, key, item):
        """
        Add an item in the cache
        """

        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """

        if key not in self.cache_data or key is None:
            return None
        return self.cache_data.get(key)
