"""Utility Function Exercise."""

__author__ = "730411655"


def only_evens(x: list[int]) -> list[int]:
    """The inputed integers return the even integers of a list."""
    evens_list: list[int] = []
    for item in x:
        if item % 2 == 0:
            evens_list.append(item)
    return evens_list


def sub(x: list[int], start: int, end: int) -> list[int]:
    """Two integers will create a subset of a list. """
    sub_list: list[int] = []
    if start < 0:
        start = 0
    if end > len(x):
        end = len(x) - 1
    if len(x) == 0 or start > end or end <= 0:
        return sub_list
    while start < end:
        sub_list.append(x[start])
        start += 1
    return sub_list


def concat(a: list[int], b: list[int]) -> list[int]:
    """Generates a new list from two different lists."""
    concat_list: list[int] = []
    i = 0
    while i < len(a): 
        concat_list.append(a[i])
        i += 1
    i = 0
    while i < len(b): 
        concat_list.append(b[i])
        i += 1

    return concat_list
