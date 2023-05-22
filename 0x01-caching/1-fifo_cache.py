#!/usr/bin/env python3
""" Script -> FIFO caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Assigns the new item to the dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_in = next(iter(self.cache_data))
                del self.cache_data[first_in]
                print(f'DISCARD: {first_in}')

    def get(self, key):
        """ Returns the value in self.cache_data linked to key """
        return self.cache_data.get(key, None)
