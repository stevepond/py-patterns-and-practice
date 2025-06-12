from data_structures.problem_19_pair_sum import pair_sum


def test_pair_sum():
    assert pair_sum([1,2,3], 5)
    assert not pair_sum([1,2], 5)
