#!/usr/bin/python3
""" 3-main """
LRUCache = __import__('3-lru_cache').LRUCache

my_cache = LRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
# DISCARD: A
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A")) # # None
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
# DISCARD: D
my_cache.print_cache()
my_cache.put("G", "San Francisco")
# DISCARD: E
my_cache.print_cache()
my_cache.put("H", "H")
# DISCARD: B
my_cache.print_cache()
my_cache.put("I", "I")
# DISCARD: C
my_cache.print_cache()
my_cache.put("J", "J")
# DISCARD: F
my_cache.print_cache()
my_cache.put("K", "K")
# DISCARD: G
my_cache.print_cache()
