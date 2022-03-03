"""Testing my dictionary functions."""

from dictionary import invert
from dictionary import favorite_color
from dictionary import count


def test_invert_double() -> None:
    """Tests if given inputs become dictionaries."""
    assert invert({'bob': '1', 'evan': '2'}) == {'1': 'bob', '2': 'evan'}


def test_invert_again() -> None:
    """Tests if given inputs become dictionaries."""
    assert invert({'a': 'b', 'c': 'd'}) == {'b': 'a', 'd': 'c'}

    
def test_invert_error() -> None:
    """Tests if given inputs become dictionaries."""
    import pytest
    with pytest.raises(KeyError):
        my_dictionary = {'jake': 'fin', 'bob': 'fin'}
        invert(my_dictionary)


def test_favorite_color_multiple() -> None:
    """Tests if the most popular color is returned."""
    color_options: dict[str, str] = {'Mark': 'blue', 'Zoe': 'blue', 'Brad': 'blue', 'Cary': 'green'}
    assert favorite_color(color_options) == 'blue'


def test_favorite_color_again() -> None:
    """Tests if the most popular color is returned."""
    color_options: dict[str, str] = {'Mark': 'red', 'Zoe': 'red', 'Brad': 'red', 'Cary': 'red'}
    assert favorite_color(color_options) == 'red'


def test_favorite_color_edge() -> None:
    """Tests if the most popular color is returned."""
    color_options: dict[str, str] = {'Mark': 'blue', 'Zoe': 'blue', 'Brad': 'green', 'Cary': 'green'}
    assert favorite_color(color_options) == 'blue'


def test_count_single() -> None:
    """Test if inputs are counted correctly."""
    count_i: list[str] = ["mark", "brad", "susan", "mary"]
    assert count(count_i) == {'mark': 1, 'brad': 1, 'susan': 1, 'mary': 1}


def test_count_multiple() -> None:
    """Test if inputs are counted correctly."""
    count_i: list[str] = ["mark", "brad", "mark", "mary"]
    assert count(count_i) == {'mark': 2, 'brad': 1, 'mary': 1}


def test_count_again() -> None:
    """Test if inputs are counted correctly."""
    count_i: list[str] = ["donuts", "donuts", "pizza", "pizza"]
    assert count(count_i) == {'donuts': 2, 'pizza': 2}