#!/usr/bin/env python3
"""Script -> index_range function"""

def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of size two containing a start index & end index."""
    start = (page - 1) * page_size
    end = start + page_size
    return start, end
