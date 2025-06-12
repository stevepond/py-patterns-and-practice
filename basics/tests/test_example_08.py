from basics.example_08 import index_items


def test_index_items():
    assert index_items(['a', 'b']) == [(0, 'a'), (1, 'b')]
