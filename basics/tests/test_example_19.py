from basics.example_19 import Point


def test_point_dataclass():
    p = Point(1, 2)
    assert p.x == 1 and p.y == 2
