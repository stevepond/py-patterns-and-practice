from data_structures.problem_07_binary_tree import BinaryTree


def test_binary_tree_insert_inorder():
    bt = BinaryTree()
    for v in [2, 1, 3]:
        bt.insert(v)
    assert bt.inorder() == [1, 2, 3]
