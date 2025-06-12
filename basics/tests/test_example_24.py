"""
Tests for Dictionary Iteration
"""
from basics.example_24 import (
    person, uppercase_values,
    string_values, entries
)

def test_dictionary_iteration():
    # Test original dictionary
    assert person == {
        "name": "John",
        "age": 30,
        "city": "New York",
        "occupation": "Developer"
    }
    
    # Test uppercase values
    assert uppercase_values == {
        "name": "JOHN",
        "age": 30,
        "city": "NEW YORK",
        "occupation": "DEVELOPER"
    }
    
    # Test string values filter
    assert string_values == {
        "name": "John",
        "city": "New York",
        "occupation": "Developer"
    }
    
    # Test entries list
    assert entries == [
        ("name", "John"),
        ("age", 30),
        ("city", "New York"),
        ("occupation", "Developer")
    ] 