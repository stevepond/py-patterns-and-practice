from basics.example_20 import Circle
import pytest


def test_circle_property():
    c = Circle(1)
    c.radius = 2
    assert c.radius == 2
    with pytest.raises(ValueError):
        c.radius = -1
