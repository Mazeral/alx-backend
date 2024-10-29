#!/usr/bin/env python3

"""
Module implementing fifo_caching.

Provides a FIFO caching implementation with put and get methods.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    A FIFO caching class inheriting from BaseCaching.

    Attributes:
        cache_data (dict): The dictionary storing cached items.
    """

    def __init__(self):
        """
        Initializes the FIFOCache instance.

        Calls the parent class's __init__ method.
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to the FIFO cache.

        Args:
            key (any): The key for the item.
            item (any): The item to be cached.

        Notes:
            If key or item is None, this method does not cache the item.
            If cache is full, discards the first item (FIFO algorithm).
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            print(f"DISCARD: {first_key}")
            del self.cache_data[first_key]

        if key not in self.cache_data:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the FIFO cache.

        Args:
            key (any): The key for the item.

        Returns:
            any: The cached item if the key exists, otherwise None.
        """
        return self.cache_data.get(key)
