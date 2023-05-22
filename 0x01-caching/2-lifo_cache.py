#!/usr/bin/env python3
""" LIFO caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache """

    def ____(self):
        """ Initialize LIFOCache """
        super().__init__()
        self.history = []

    def put(self, key, item):
        """ Assigns the new item to the dictionary """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print(f'DISCARD: {self.history[-1]}')
                self.cache_data.pop(self.history[-1])
                del self.history[-1]
            if key in self.history:
                del self.history[self.history.index(key)]
            self.history.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Returns the value in self.cache_data linked to key """
        return self.cache_data.get(key, None)
