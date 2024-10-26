#!/usr/bin/env python3
"""
Module for a index_range function that Calculates
the start_index and the end_index of content
"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates pagination index range.

    Returns a tuple containing the start and end indexes for a
    paginated list based on the provided page number and page size.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple of (start_index, end_index) for pagination.
    """
    # Calculate the start index (0-indexed) based on the page and page size
    start_index = (page - 1) * page_size
    
    # Corrected calculation for the end index to avoid off-by-one error
    end_index = page * page_size
    
    # Return the calculated index range as a tuple
    return start_index, end_index
