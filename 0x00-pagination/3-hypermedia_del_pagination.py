#!/usr/bin/env python3
"""
Script -> deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached data-sets
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                self.__dataset = list(reader)[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at zero
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns a dict with key-value pair
        """
        assert isinstance(index, int) and index in range(len(self.indexed_dataset()))
        next_index = index + page_size
        data = []
        for i in range(index, next_index):
            if i not in self.indexed_dataset():
                next_index += 1
            else:
                data.append(self.indexed_dataset()[i])

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
        }
