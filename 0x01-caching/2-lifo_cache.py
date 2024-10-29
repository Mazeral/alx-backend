#!/usr/bin/env python3

"""
Module implementing LIFOCaching.

Provides a LIFO caching implementation with put and get methods.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    A LIFO caching class inheriting from BaseCaching.

    Attributes:
        cache_data (dict): The dictionary storing cached items.
    """

    def __init__(self):
        """
        Initializes the LIFOCache instance.

        Calls the parent class's __init__ method.
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to the LIFO cache.

        Args:
            key (any): The key for the item.
            item (any): The item to be cached.

        Notes:
            If key or item is None, this method does not cache the item.
            If cache is full, discards the last item (LIFO algorithm).
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            print(f"DISCARD: {last_key}")
            del self.cache_data[last_key]

        self.cache_data[key] = item  # Overwrite if key already exists

    def get(self, key):
        """
        Retrieves an item from the LIFO cache.

        Args:
            key (any): The key for the item.

        Returns:
            any: The cached item if the key exists, otherwise None.
        """
        return self.cache_data.get(key)
