"""In Class Love Function Examples."""


def love(name: str) -> str:
    """Given a names as a parameter, returns a loving string."""
    return f"I love you {name}! "


def spread_love(to: str, n: int) -> str:
    """Generates string that repeats a loving message n times."""
    love_note: str = ""
    i: int = 0
    while i < n:
        love_note += love(to) + "\n"
        i += 1
    return love_note
