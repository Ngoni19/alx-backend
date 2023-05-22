#!/usr/bin/env python3
""" Script-> LRU caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache """

    definit__(self):
        """ Initialize LRUCache """
        super().__init__()
        self.history = []

    def put(self, key, item):
        """ Assigns the new item to the dictionary """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS
                 and key not in self.cache_data:
                print(f'DISCARD: {self.history[0]}')
                del self.cache_data[self.history[0]]
                del self.history[0]
            if key in self.history:
                self.history.remove(key)
            self.history.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Returns the value in self.cache_data linked to key """
        if key is not None and key in self.cache_data:
            self.history.remove(key)
            self.history.append(key)
            return self.cache_data[key]
        return None
