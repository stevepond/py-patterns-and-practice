from data_structures.problem_12_tree_depth import Node, max_depth


def test_max_depth():
    root = Node(1, Node(2), Node(3, Node(4)))
    assert max_depth(root) == 3
