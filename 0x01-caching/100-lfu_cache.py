length = len(self.cache_data)
if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
