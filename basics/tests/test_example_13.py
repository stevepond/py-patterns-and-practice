from basics.example_13 import count_letters


def test_count_letters():
    result = count_letters(['ab', 'a'])
    assert result['a'] == 2 and result['b'] == 1
