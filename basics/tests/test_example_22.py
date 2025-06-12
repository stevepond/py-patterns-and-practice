"""
Tests for If/Else Statements and Ternary Operations
"""
from basics.example_22 import (
    age, status, score, grade,
    message, is_weekend, is_holiday,
    activity, month, season
)

def test_conditional_statements():
    assert age == 20
    assert status == "adult"
    assert score == 85
    assert grade == "B"
    assert message == "Adult B"
    assert is_weekend is True
    assert is_holiday is False
    assert activity == "relax"
    assert month == "July"
    assert season == "summer" 