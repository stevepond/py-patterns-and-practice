from pathlib import Path
from basics.example_04 import write_and_read


def test_write_and_read(tmp_path):
    file_path = tmp_path / "sample.txt"
    assert write_and_read(file_path, "hello") == "hello"
