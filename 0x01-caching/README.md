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

### How to Run
- Clone the repository:
  ```
  git clone https://github.com/your-username/alx-backend
  cd alx-backend/0x01-caching
  ```

- Run the test scripts:
  ```
  python3 0-main.py   # For BasicCache
  python3 1-main.py   # For FIFOCache
  python3 2-main.py   # For LIFOCache
  python3 3-main.py   # For LRUCache
  python3 4-main.py   # For MRUCache
  ```

### Repository Structure

```bash
alx-backend/
├── 0x01-caching/
│   ├── 0-basic_cache.py
│   ├── 1-fifo_cache.py
│   ├── 2-lifo_cache.py
│   ├── 3-lru_cache.py
│   ├── 4-mru_cache.py
│   ├── 0-main.py
│   ├── 1-main.py
│   ├── 2-main.py
│   ├── 3-main.py
│   └── 4-main.py
```

### Author
- **Mohammad Omar Siddiq**
