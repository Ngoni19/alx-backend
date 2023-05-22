#!/usr/bin/env python3
""" Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ A basic caching that inherits from BaseCaching """

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache """
        return self.cache_data.get(key, None)
