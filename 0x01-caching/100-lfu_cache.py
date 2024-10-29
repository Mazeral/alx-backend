#!/usr/bin/env python3

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    An LRU caching class inheriting from BaseCaching.

    Attributes:
        cache_data (dict): The dictionary storing cached items.
        LRU (list): A list tracking the order of recently used keys.
    """

    def __init__(self):
        """
        Initializes the LRUCache instance.

        Calls the parent class's __init__ method and sets up the LRU list.
        """
        super().__init__()
        self.LRU = {}

    def put(self, key, item):
        """
        Adds an item to the LRU cache.

        If key or item is None, this method does not cache the item.
        If the number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS,
        discards the least recently used item (LRU algorithm) and prints a
        DISCARD message.

        Args:
            key (any): The key for the item.
            item (any): The item to be cached.
        """
        if key is None or item is None:
            return

        if key in self.cache_data.keys():
            self.cache_data[key] = item
            self.LRU[key] += 1
            return

        if self.MAX_ITEMS <= len(self.cache_data.items()):
            smallest_key = min(self.LRU, key=self.LRU.get)
            print(f"DISCARD: {smallest_key}")
            del self.cache_data[smallest_key]
            del self.LRU[smallest_key]

        self.cache_data[key] = item
        self.LRU[key] = 1

    def get(self, key):
        """
        Retrieves an item from the LRU cache.

        If the key exists, updates its position in the LRU list.

        Args:
            key (any): The key for the item.

        Returns:
            any: The cached item if the key exists, otherwise None.
        """
        if key in self.cache_data.keys():
            self.LRU[key] += 1
            return self.cache_data[key]
        return None
