"""Dictionary related utility functions."""

__author__ = "730411655"
from csv import DictReader
# Define your functions below


def read_csv_rows(nc_durham_2015_march_21_to_26: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    file_handle = open(nc_durham_2015_march_21_to_26, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)
    
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all vlaues in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result 


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(n: dict[str, list[str]], count_rows: int) -> dict[str, list[str]]:
    """Produces a new column table with just the first N rows of data of each column."""
    result: dict[str, list[str]] = {}
    for item in n:
        i = 0 
        if len(n[item]) < count_rows:
            count_rows = len(n[item])
        values: list[str] = []
        while i < count_rows:
            values.append(n[item][i])
            i += 1
        result[item] = values     

    return result


def select(a: dict[str, list[str]], name: list[str]) -> dict[str, list[str]]:
    """Produce a column based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column in name:
        result[column] = a[column]
    return result


def concat(a: dict[str, list[str]], b: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column table with 2 column tables combined."""
    result: dict[str, list[str]] = {}
    for column in a:
        result[column] = a[column]
    for column in b:
        if column in result:
            i = 0
            while i < len(b[column]):
                result[column].append(b[column][i])
                i += 1
        else:
            result[column] = b[column]
    return result
    

def count(counter: list[str]) -> dict[str, int]: 
    """Given a list, will produce a dictionary with unique values assocaiated to the number of times that value appears."""
    result: dict[str, int] = {}
    for item in counter:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


    
