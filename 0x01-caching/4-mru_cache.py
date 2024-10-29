#!/usr/bin/env python3

"""
Module implementing MRUCache (Most Recently Used).

Provides an MRU caching implementation with put and get methods.
"""

from base_caching import BaseCaching


def move_to_zero(lst, i):
    """
    Moves an element to the beginning of a list.

    Args:
        lst (list): The input list.
        i (int): The index of the element to move.

    Returns:
        list: The modified list with the element at the beginning.
    """
    return [lst[i]] + [x for j, x in enumerate(lst) if j != i]


class MRUCache(BaseCaching):
    """
    An MRU caching class inheriting from BaseCaching.

    Attributes:
        cache_data (dict): The dictionary storing cached items.
        MRU (list): A list tracking the order of recently used keys.
    """

    def __init__(self):
        """
        Initializes the MRUCache instance.

        Calls the parent class's __init__ method and sets up the MRU list.
        """
        super().__init__()
        self.MRU = []

    def put(self, key, item):
        """
        Adds an item to the MRU cache.

        If key or item is None, this method does not cache the item.
        If the number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS,
        discards the most recently used item (MRU algorithm) and prints a
        DISCARD message.

        Args:
            key (any): The key for the item.
            item (any): The item to be cached.
        """
        if key is None or item is None:
            return

        if key in self.cache_data.keys():
            self.cache_data[key] = item
            return

        if self.MAX_ITEMS <= len(self.cache_data.items()):
            print(f"DISCARD: {self.MRU[0]}")
            del self.cache_data[self.MRU[0]]
            self.MRU.pop(0)

        self.cache_data[key] = item
        self.MRU.insert(0, key)

    def get(self, key):
        """
        Retrieves an item from the MRU cache.

        If the key exists, updates its position in the MRU list.

        Args:
            key (any): The key for the item.

        Returns:
            any: The cached item if the key exists, otherwise None.
        """
        if key in self.cache_data.keys():
            self.MRU = move_to_zero(self.MRU, self.MRU.index(key))
            return self.cache_data[key]
        return None
