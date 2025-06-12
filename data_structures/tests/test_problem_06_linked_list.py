from data_structures.problem_06_linked_list import LinkedList


def test_linked_list():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    assert ll.to_list() == [1, 2]
