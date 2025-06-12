from data_structures.problem_20_palindrome import is_palindrome


def test_is_palindrome():
    assert is_palindrome('level')
    assert not is_palindrome('python')
