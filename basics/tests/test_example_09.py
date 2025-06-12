from basics.example_09 import pair_lists


def test_pair_lists():
    assert pair_lists([1, 2], ['a', 'b']) == [(1, 'a'), (2, 'b')]
