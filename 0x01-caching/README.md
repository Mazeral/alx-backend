# Caching Systems - README

## Overview
This repository contains several caching system implementations as part of the **alx-backend** project. Each caching system is implemented as a class that inherits from `BaseCaching`. These systems demonstrate different cache eviction strategies such as FIFO (First In, First Out), LIFO (Last In, First Out), LRU (Least Recently Used), and MRU (Most Recently Used). The caching mechanism is implemented using a dictionary (`self.cache_data`), which is inherited from `BaseCaching`.

### Requirements
- Python 3.x
- Must follow PEP8 style guidelines
- Inherits `BaseCaching` class for core functionality
- Each caching class must implement the `put()` and `get()` methods.

### Tasks

#### 0. Basic Dictionary (No limit cache)
File: `0-basic_cache.py`

- **Class**: `BasicCache`
- This is a basic caching system with no size limit. It stores key-value pairs in the dictionary `self.cache_data`.
- **Methods**:
  - `put(key, item)`: Adds or updates the value in the cache for the given `key`. If `key` or `item` is `None`, it does nothing.
  - `get(key)`: Retrieves the value associated with `key`. If `key` is `None` or doesn't exist, it returns `None`.

#### 1. FIFO Caching
File: `1-fifo_cache.py`

- **Class**: `FIFOCache`
- Implements a cache that uses the **First In, First Out (FIFO)** strategy. If the cache exceeds the `MAX_ITEMS` limit, the oldest item is removed from the cache.
- **Methods**:
  - `put(key, item)`: Adds a new `key` and `item` to the cache. If the cache exceeds `MAX_ITEMS`, the first added item is discarded, and the key is printed as `DISCARD: {key}`.
  - `get(key)`: Retrieves the value associated with `key`. If `key` is `None` or doesn't exist, it returns `None`.

#### 2. LIFO Caching
File: `2-lifo_cache.py`

- **Class**: `LIFOCache`
- Implements a cache using the **Last In, First Out (LIFO)** strategy. When the cache reaches `MAX_ITEMS`, the most recently added item is discarded.
- **Methods**:
  - `put(key, item)`: Adds a new `key` and `item` to the cache. If the cache exceeds `MAX_ITEMS`, the most recently added item is discarded, and the key is printed as `DISCARD: {key}`.
  - `get(key)`: Retrieves the value associated with `key`. If `key` is `None` or doesn't exist, it returns `None`.

#### 3. LRU Caching
File: `3-lru_cache.py`

- **Class**: `LRUCache`
- Implements a **Least Recently Used (LRU)** caching system. The least recently accessed item is removed when the cache exceeds the `MAX_ITEMS` limit.
- **Methods**:
  - `put(key, item)`: Adds a new `key` and `item` to the cache. If the cache exceeds `MAX_ITEMS`, the least recently used item is discarded, and the key is printed as `DISCARD: {key}`.
  - `get(key)`: Retrieves the value associated with `key`. If the key is accessed, it is marked as "recently used". If `key` is `None` or doesn't exist, it returns `None`.

#### 4. MRU Caching
File: `4-mru_cache.py`

- **Class**: `MRUCache`
- Implements a **Most Recently Used (MRU)** caching system. The most recently accessed item is removed when the cache exceeds the `MAX_ITEMS` limit.
- **Methods**:
  - `put(key, item)`: Adds a new `key` and `item` to the cache. If the cache exceeds `MAX_ITEMS`, the most recently used item is discarded, and the key is printed as `DISCARD: {key}`.
  - `get(key)`: Retrieves the value associated with `key`. If `key` is accessed, it is marked as "most recently used". If `key` is `None` or doesn't exist, it returns `None`.

## Advanced Tasks

### 5. LFU Caching

**File:** `100-lfu_cache.py`

- A caching system implementing the **Least Frequently Used (LFU)** algorithm.
- Discards the least frequently used item when the cache exceeds its maximum size.
- If multiple items have the same usage frequency, the **Least Recently Used (LRU)** algorithm is applied to discard the least recently accessed item.
- The `put` and `get` methods handle both frequency and recency to ensure proper eviction.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/alx-backend.git
   ```

2. Navigate to the project directory:
   ```bash
   cd 0x01-caching
   ```

3. Run the main Python file for each caching system to test the functionality:
   ```bash
   python3 0-main.py  # For Basic Dictionary
   python3 1-main.py  # For FIFO Caching
   python3 2-main.py  # For LIFO Caching
   python3 3-main.py  # For LRU Caching
   python3 4-main.py  # For MRU Caching
   python3 100-main.py  # For LFU Caching
   ```

### Author
- **Mohammad Omar Siddiq**
