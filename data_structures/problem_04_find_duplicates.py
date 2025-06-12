"""Problem 04: Find duplicates in list"""

def find_duplicates(lst):
    """Return set of duplicated items."""
    seen = set()
    dupes = set()
    for item in lst:
        if item in seen:
            dupes.add(item)
        else:
            seen.add(item)
    return dupes
