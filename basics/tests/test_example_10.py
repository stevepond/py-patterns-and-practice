from basics.example_10 import count_up_to


def test_count_up_to():
    assert list(count_up_to(3)) == [1, 2, 3]
