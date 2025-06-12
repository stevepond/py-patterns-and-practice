"""Example 13: defaultdict"""

from collections import defaultdict

def count_letters(words):
    """Count letters using defaultdict."""
    counter = defaultdict(int)
    for word in words:
        for letter in word:
            counter[letter] += 1
    return dict(counter)
