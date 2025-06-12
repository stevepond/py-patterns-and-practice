from data_structures.problem_04_find_duplicates import find_duplicates


def test_find_duplicates():
    assert find_duplicates([1, 2, 2, 3, 1]) == {1, 2}
