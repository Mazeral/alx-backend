#!/usr/bin/env python3

"""
A module containing the BasicCache class.

Provides a basic caching implementation with put and get methods.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A basic caching class inheriting from BaseCaching.

    Attributes:
        cache_data (dict): The dictionary storing cached items.
    """

    def __init__(self):
        """
        Initializes the BasicCache instance.

        Calls the parent class's __init__ method.
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to the cache.

        Args:
            key (any): The key for the item.
            item (any): The item to be cached.

        Notes:
            If key or item is None, this method does not cache the item.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache.

        Args:
            key (any): The key for the item.

        Returns:
            any: The cached item if the key exists, otherwise None.
        """
        return self.cache_data.get(key)
