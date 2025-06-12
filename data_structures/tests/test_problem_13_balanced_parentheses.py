from data_structures.problem_13_balanced_parentheses import is_balanced


def test_is_balanced():
    assert is_balanced('(())')
    assert not is_balanced('(()')
