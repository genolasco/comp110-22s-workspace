"""Example of a function that searches through a list. """


def main() -> None:
    print(contains("Kevin Baconn", ["Kanye West", "Pete Davidson"]))

# Define a function named contains 
# two parameters:
# 1. needle - the string we're searching for
# 2. haystack - the list we're serarching through


def contains(needle: str, haystack: list[str]) -> bool:
    # Algorithem:
    # Fore ach item in the haystack
    #       Test if it is  equal to the needle
    #        IF so, return True
    for item in haystack:
        if item == needle:
            return True
    # After testing all item, return False, because not found
    # Returns true if neele in haystack, false otherwise
    return False


if __name__ == "__main__":
    main()