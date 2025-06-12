from algorithms.problem_01_binary_search import binary_search


def test_binary_search():
    arr = [1, 2, 3, 4, 5]
    assert binary_search(arr, 3) == 2
    assert binary_search(arr, 6) == -1

