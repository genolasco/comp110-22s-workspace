"""Exercise practicing dictionary functions."""

__author__ = "730411655"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Returns given imputs into dictionaries."""
    my_dict: dict[str, str] = {}
    for key in x:
        my_dict_key = x[key]
        my_dict[my_dict_key] = key
    if len(x) != len(my_dict):
        raise KeyError("Error: Unable to compute.")

    return my_dict


def favorite_color(x: dict[str, str]) -> str:
    """Returns the most popular color."""
    popular_color: str = ""
    my_dict: dict[str, int] = {}
    for key in x:
        colors: str = x[key]
        if colors in my_dict:
            my_dict[colors] += 1
        else:
            my_dict[colors] = 1
    max = 0
    for color in my_dict:
        if my_dict[color] > max:
            max = my_dict[color]
            popular_color = color
            
    return popular_color 


def count(x: list[str]) -> dict[str, int]:
    """Counts inputs given."""
    my_dict: dict[str, int] = {}
    for item in x:
        if item in my_dict:
            my_dict[item] += 1
        else:
            my_dict[item] = 1

    return my_dict
