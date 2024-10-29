#!/usr/bin/env python3

"""
Module implementing LRUCache (Least Recently Used).

Provides an LRU caching implementation with put and get methods.
"""

from base_caching import BaseCaching


def move_to_zero(lst, index):
    """
    Moves an element to the beginning of a list.

    Args:
        lst (list): The input list.
        index (int): The index of the element to move.

    Returns:
        list: The modified list with the element at the beginning.
    """
    return [lst[index]] + [x for i, x in enumerate(lst) if i != index]


class LRUCache(BaseCaching):
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
        self.LRU = []

    def put(self, key, item):
        """
        Adds an item to the LRU cache.

        Args:
            key (any): The key for the item.
            item (any): The item to be cached.

        Notes:
            If key or item is None, this method does not cache the item.

            If cache is full, discards the least recently used item
            (LRU algorithm).
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.LRU.remove(key)
            self.LRU.insert(0, key)
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            discarded_key = self.LRU.pop()
            print(f"DISCARD: {discarded_key}")
            del self.cache_data[discarded_key]

        self.cache_data[key] = item
        self.LRU.insert(0, key)

    def get(self, key):
        """
        Retrieves an item from the LRU cache.

        Args:
            key (any): The key for the item.

        Returns:
            any: The cached item if the key exists, otherwise None.
        """
        if key in self.cache_data:
            self.LRU = move_to_zero(self.LRU, self.LRU.index(key))
            return self.cache_data[key]
        return None
