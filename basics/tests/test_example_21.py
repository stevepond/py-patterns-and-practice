"""
Tests for JavaScript Array Method Equivalents
"""
from basics.example_21 import (
    numbers, doubled, doubled_comprehension,
    sum_numbers, sum_reduce,
    first_greater_than_3,
    greater_than_3, greater_than_3_comprehension,
    has_greater_than_3, all_positive
)

def test_array_methods():
    assert numbers == [1, 2, 3, 4, 5]
    assert doubled == [2, 4, 6, 8, 10]
    assert doubled_comprehension == [2, 4, 6, 8, 10]
    assert sum_numbers == 15
    assert sum_reduce == 15
    assert first_greater_than_3 == 4
    assert greater_than_3 == [4, 5]
    assert greater_than_3_comprehension == [4, 5]
    assert has_greater_than_3 is True
    assert all_positive is True 