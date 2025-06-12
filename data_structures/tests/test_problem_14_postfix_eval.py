from data_structures.problem_14_postfix_eval import eval_postfix


def test_eval_postfix():
    assert eval_postfix(['2', '3', '+', '4', '*']) == 20
