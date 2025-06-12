from basics.example_05 import add_one


def test_add_one_decorated():
    assert add_one(1) == 2
