from basics.example_03 import format_kwargs


def test_format_kwargs():
    result = format_kwargs(a=1, b=2)
    assert "a=1" in result and "b=2" in result
