from data_structures.problem_05_word_count import word_count


def test_word_count():
    assert word_count('a b a') == {'a': 2, 'b': 1}
