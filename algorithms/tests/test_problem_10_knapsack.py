from algorithms.problem_10_knapsack import knapsack


def test_knapsack():
    w = [1,2,3]
    v = [6,10,12]
    assert knapsack(w, v, 5) == 22

