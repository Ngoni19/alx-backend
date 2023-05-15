#!/usr/bin/env python3
"""Script -> simple pagination"""
import csv
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of size two containing a start index & end index"""
    start = (page - 1) * page_size
    return (start, start + page_size)


class Server:
    """Class- Server class to paginate a database of popular baby names.
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
                self.__dataset = list(reader)[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """finds the correct indexes to paginate the dataset \
            correctly & return the appropriate page of the dataset
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start = (page - 1) * page_size
        end = start + page_size
        dataset = self.dataset()
        return dataset[start:end] if start < len(dataset) else []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """returns an hypermedia object based on self.get_page result"""
        page_data = self.get_page(page, page_size)
        total_pages = (len(self.dataset()) + page_size - 1) // page_size
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(page_data),
            "page": page,
            "data": page_data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
