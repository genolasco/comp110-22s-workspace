"""Testing Utility Fuctions Exercise."""

__author__ = "730411655"

from utils import only_evens
from utils import sub
from utils import concat


def test_only_evens_single() -> None:
    """The inputed integers return the even integers of a list."""
    assert only_evens([1, 2, 3, 4, 5]) == [2, 4]


def test_only_evens_multiple() -> None:
    """The inputed integers return the even integers of a list."""
    x = 2
    assert only_evens([x]) == [2]


def test_only_evens_again() -> None:
    """The inputed integers return the even integers of a list."""
    x = [-31, -20, -15]
    assert only_evens(x) == [-20]


def test_sub_single() -> None:
    """Two integers will create a subset of a list."""
    x = [-11, 1, 2, 3, 4]
    start = -1
    end = 3
    assert sub(x, start, end) == [1, 2]


def test_sub_multiple() -> None:
    """Two integers will create a subset of a list."""
    x = [0, 1, 2, 3, 4]
    start = 0
    end = 3
    assert sub(x, start, end) == [1, 2]


def test_sub_again() -> None:
    """Two integers will create a subset of a list."""
    x = [1, 2, 3, 4]
    start = 1
    end = 5
    assert sub(x, start, end) == [2, 3, 4]


def test_concat_single() -> None:
    """Generates a new list from sub and only_evens."""
    a = [1, 2]
    b = [3, 4]
    assert concat(a, b) == [1, 2, 3, 4]


def test_concate_multiple() -> None:
    """Generates a new list from sub and only_evens."""
    a = []
    b = [1, 2]
    assert concat(a, b) == [1, 2]


def test_concate_again() -> None:
    """Generates a new list from  two different lists."""
    a = [-20, 30, 50]
    b = [-20, 30, 50]
    assert concat(a, b) == [-20, 30, 50, -20, 30, 50]
