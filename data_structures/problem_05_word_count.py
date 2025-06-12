"""Problem 05: Word count using dict"""

def word_count(text):
    """Return dict of word frequencies."""
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts
