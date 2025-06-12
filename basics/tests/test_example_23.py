"""
Tests for While Loops
"""
from basics.example_23 import numbers, validate_age

def test_while_loop_results():
    # Test the final state of the numbers list
    assert numbers == [1, 2, 3, 4, 5]
    
    # Note: The other examples in example_23.py are primarily
    # demonstration examples that print output or take user input,
    # so they don't have easily testable return values.
    # In a real application, you would want to refactor those
    # examples to return values that can be tested. 

def test_validate_age():
    # Test valid ages
    assert validate_age("20") is True
    assert validate_age("0") is True
    assert validate_age("120") is True
    
    # Test invalid ages
    assert validate_age("-1") is False
    assert validate_age("121") is False
    assert validate_age("abc") is False
    assert validate_age("") is False 