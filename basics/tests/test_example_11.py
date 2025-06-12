from basics.example_11 import open_file


def test_open_file(tmp_path):
    file_path = tmp_path / "data.txt"
    with open_file(file_path, "w") as f:
        f.write("x")
    with open_file(file_path) as f:
        assert f.read() == "x"
