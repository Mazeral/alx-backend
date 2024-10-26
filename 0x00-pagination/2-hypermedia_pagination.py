import csv
import math
from typing import List, Tuple
"""
Module for Server class for hypermedia pagination
"""


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a paginated subset of the dataset.

        Args:
            page (int, optional): The page number (1-indexed). Defaults to 1.
            page_size (int, optional): The number of items per page. Defaults
            to 10.

        Returns:
            List[List[str]]: The paginated subset of the dataset.

        Raises:
            AssertionError: If page or page_size is not a positive integer.
        """
        assert (isinstance(page, int) and isinstance(page_size, int))
        assert (page > 0 and page_size > 0 and
                isinstance(page, int) and
                isinstance(page_size, int))
        assert page > 0 and page_size > 0 and (page != 0 or page_size != 0)
        # using the function we made earlier!
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Retrieves a paginated dataset page with metadata.

        Args:
            page (int, optional): The page number (1-indexed). Defaults to 1.
            page_size (int, optional): The number of items per page.
            Defaults to 10.

        Returns:
            dict: A dictionary containing pagination metadata and the dataset
            page.
        """
        start, end = index_range(page, page_size)

        # Calculate total pages based on the dataset length
        total_pages = -(-len(self.dataset()) // page_size)  # Ceiling division

        return {
            'page_size': page_size,
            'page': page,
            'data': self.dataset()[start:end],
            'next_page': page + 1
            if len(self.dataset()) > page * page_size
            else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
